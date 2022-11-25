import cv2
from PIL import Image
import os
import re
import sys

# imgディレクトリパス
imgPath = '../img'
# 結果格納パス
resultPath = '../results'

# テスト画像の準備
# 画像ファイル取得
fileExtension = '.+\.(jpg|jpeg|png|HEIC)'
pattern = re.compile(fileExtension)

images = []
for item in os.listdir(imgPath):
    result = pattern.match(item)
    # resultがNone以外=画像 なのでパスをリストに追加
    if result:
        images.append(imgPath + '/' + item)

for image in images:
    print(image)
    img = cv2.imread(image)

    # img_gauss = cv2.GaussianBlur(img, (3, 3), sigmaX=3)
    img_gauss = cv2.GaussianBlur(img, (5, 5), 0)
    # ret , tho = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    wroteFile = imgPath + "/blur_" + os.path.basename(image)
    cv2.imwrite(wroteFile, img_gauss)
