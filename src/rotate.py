import cv2
from PIL import Image
import os
import re
import sys

# imgディレクトリパス
imgPath = '../pdf2img'
# 結果格納パス
resultPath = '../pdf2img'

# テスト画像の準備
# 画像ファイル取得
fileExtension = '.+\.(jpg|jpeg|png|HEIC)'
pattern = re.compile(fileExtension)

# 左に90度回転している画像を設定
image_names = [
    '3_20221130212135002.png',
    '4_20221130212135002.png',
    '5_20221130212135002.png',
    '6_20221130212135002.png',
    '7_20221130212135002.png',
]

for image_name in image_names:
    img = cv2.imread(imgPath + '/' + image_name)

    img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(resultPath + '/' + image_name, img_rotate_90_clockwise)

