import cv2
from PIL import Image
from PyPDF2 import PdfReader
import os
import re

# imgディレクトリパス
pdfPath = '../pdf'
# 結果格納パス
resultPath = '../pdf2img'

# tiff->pdf変換tmpファイル
tmpFile = 'tmp.tiff'

# テスト画像の準備
# 画像ファイル取得
fileExtension = '.+\.pdf'
pattern = re.compile(fileExtension)

pdfs = []
for item in os.listdir(pdfPath):
    result = pattern.match(item)
    # resultがNone以外=画像 なのでパスをリストに追加
    if result:
        pdfs.append(pdfPath + '/' + item)

for pdf in pdfs:
    reader = PdfReader(pdf)
    count = 0

    for page in reader.pages:
        for image_file_object in page.images:
            with open('tmp.tiff', "wb") as fp:
                fp.write(image_file_object.data)

            path = resultPath + '/' + str(count) + '_' + os.path.splitext(os.path.basename(pdf))[0] + '.png'
            img = cv2.imread(tmpFile)
            cv2.imwrite(path, img)
            count += 1

#  tmpファイルの削除
os.remove(tmpFile)
