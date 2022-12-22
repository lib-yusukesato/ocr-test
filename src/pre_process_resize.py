import cv2
from PIL import Image
import os
import re

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

    scale = 3
    resized = cv2.resize(img, (img.shape[1]*scale, img.shape[0]*scale), interpolation=cv2.INTER_CUBIC)

    wroteFile = imgPath + "/resize_" + os.path.basename(image)
    cv2.imwrite(wroteFile, resized)
