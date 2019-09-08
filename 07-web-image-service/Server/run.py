from flask import Flask, request
from flask_cors import CORS, cross_origin
import base64
import cv2
import numpy as np

app = Flask('CV-Web')
CORS(app)

def cv_engine(img, operation):
    if operation == 'to_grayscale':
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif operation == 'get_edge_canny':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        canny_edges = cv2.Canny(gray, 100, 200, 3)
        return canny_edges
    elif operation == 'get_edge_sobel':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        x_edges = cv2.Sobel(gray, -1, 1, 0, ksize = 5)
        y_edges = cv2.Sobel(gray, -1, 0, 1, ksize = 5)
        edges = cv2.addWeighted(x_edges, 0.5, y_edges, 0.5, 0)
        return edges
    elif operation == 'get_corners':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        from skimage.feature import corner_harris, corner_subpix, corner_peaks
        from skimage import img_as_float
        from skimage.draw import circle
        import math
        # 해리스코너 계산 
        image = img_as_float(gray)
        corners = corner_harris(image)
        # 코너 응답을 가지고 이미지에서 실제 코너 계산
        coords = corner_peaks(corners, min_distance=5)
        # 코너가 에지 점인지 독립된 코너인지 결정
        coords_subpix = corner_subpix(image, coords, window_size=13)
        image_corner = np.copy(image)
        for corner in coords_subpix:
            if math.isnan(corner[0]) or math.isnan(corner[1]):
                continue
            corner = [int(x) for x in corner]
            rr, cc = circle(corner[0], corner[1], 5)
            image_corner[rr, cc] = 255 # 이 점을 흰색으로
        image = image * 255 + image_corner
        return image
    else:
        return None

def read_image(image_data):
    image_data = base64.decodebytes(image_data)
    with open('temp_image.jpg', 'wb') as f :
        f.write(image_data)
        f.close()
    img = cv2.imread('temp_image.jpg')
    return img

def encode_image(img):
    ret, data = cv2.imencode('.jpg', img)
    return base64.b64encode(data)

# 클라이언트로부터 받은 요청과 이미지 처리
@app.route('/process_image', methods=['POST'])
def process_image():
    if not request.json or 'msg' not in request.json:
        return 'Server Error!', 500
    header_len = len('data:image/jpeg;base64,')
    image_data = request.json['image_data'][header_len:].encode()
    operation = request.json['operation']
    img = read_image(image_data)
    img_out = cv_engine(img, operation)
    image_data = encode_image(img_out)
    result = {'image_data': image_data, 'msg':'Operation Completed'}
    return image_data, 200

@app.route('/')
def index():
    return 'Hello ?'

if __name__ == "__main__":
    app.run(debug=True)