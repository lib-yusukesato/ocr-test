# ocr-test
## Overview
tesseract検証リポジトリ  
imgディレクトリに配置した画像に対してorcを実行する  

## How to use  
検証する画像をimgディレクトリに配置  

コンテナ起動  
```sh
docker-compose up -d
```

OCRスクリプトの実行 
```sh
docker-compose exec python3 bash
cd src
python orc.py # ocr実行
```
orc.py実行後resultsディレクトリに読み取ったテキストファイルが出力される。  

画像前処理 
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
