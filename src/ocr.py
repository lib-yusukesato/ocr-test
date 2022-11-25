import pyocr
import pyocr.builders

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


# ocr読み取り
tools = pyocr.get_available_tools()

if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'
langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))

lang = langs[0]
print("Will use lang '%s'" % (lang))


for image in images:
    print("execute: '%s'" % (image))
    res = tool.image_to_string(Image.open(image),
                                lang="best_jpn",
                                builder=pyocr.builders.TextBuilder(tesseract_layout=6))

    # 結果をファイルに書き込み
    wroteFile = resultPath + "/" + os.path.splitext(os.path.basename(image))[0] + '.txt'
    f = open(wroteFile, 'w')
    f.writelines(res)
    f.close()


# out = cv2.imread(images[0])
# for d in res:
#     print(d.content)
#     print(d.position)
#     cv2.rectangle(out_resize, d.position[0], d.position[1], (0, 0, 255), 2)

