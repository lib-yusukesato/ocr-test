import cv2
import os
import re

# imgディレクトリパス
imgPath = '../pdf2img'
# 結果格納パス
resultPath = '../trim_img'

# テスト画像の準備
# 画像ファイル取得
fileExtension = '.+\.(jpg|jpeg|png|HEIC)'
pattern = re.compile(fileExtension)

image_names = []
for item in os.listdir(imgPath):
    result = pattern.match(item)
    # resultがNone以外=画像 なのでパスをリストに追加
    if result:
        image_names.append(imgPath + '/' + item)

for i, image_name in enumerate(image_names):
    # 画像読み込み
    img = cv2.imread(image_name)

    height, width, _ = img.shape

    if width < 2500: 
        # img[top : bottom, left : right]
        license_number = img[290 : 320, width - 570: width - 320]
        name = img[25 : 55, width - 600: width - 260]
        address = img[90 : 117, width - 600: width - 80]
    else:
        # img[top : bottom, left : right]
        license_number = img[850 : 950, width - 1700: width - 950]
        name = img[70 : 160, width - 1800: width - 780]
        address = img[265 : 345, width - 1780: width - 200]

    cv2.imwrite(resultPath + "/license_number_" + str(i) + '.png', license_number)
    cv2.imwrite(resultPath + "/name_" + str(i) + '.png', name)
    cv2.imwrite(resultPath + "/address_" + str(i) + '.png', address)
