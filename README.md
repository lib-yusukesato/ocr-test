# ocr-test
## Overview
tesseract検証リポジトリ  
### 1次検証  
調査対象画像に対し、リサイズ、平滑化の前処理を行いOCR精度調査を行った。  
### スキャン検証
1次検証より立てられた仮説より、複合機からスキャンしたpdfの精度調査を行った。  
pdfはpngに変換し、特定部分をトリミングしたものをOCRで読み取る。

## How to use  
検証する画像をimgディレクトリに配置  
検証するpdfをpdfディレクトリに配置

コンテナ起動  
```sh
docker-compose up -d
```

### OCRスクリプトの実行 
```sh
docker-compose exec python3 bash
cd src
# 必要に応じてocr.py内のimgPath、resultsPathを変更する。
python orc.py # ocr実行
```
orc.py実行後resultsディレクトリに読み取ったテキストファイルが出力される。  

### 画像前処理 
```sh
docker-compose exec python3 bash
cd src
# 画像大きく
python pre_preprocess_resize.py
# 画像平滑化
python pre_preprocess_blur.py
```
imgディレクトリに存在する画像ファイルに対して前処理した画像が追加される。  
※オリジナルには影響なし  

### pdf->png変換からトリミングまで
```sh
docker-compose exec python3 bash
cd src
# pdf->png変換
python pdf_to_png.py
# 特定の画像を右90°回転
vi rotate.py
image_names = [
+ example.png
+ test.png
]
python rotate.py
# トリミング
python trimmng.py
```

## Directory structure
img: 1次検証用画像用  
pdf: スキャン検証するpdfファイル用  
pdf2img: pdf変換した画像用  
results: 1検証結果用  
src: 実行スクリプト用  
trim_img: トリミングした画像用  
trim_results: スキャン検証結果用  
