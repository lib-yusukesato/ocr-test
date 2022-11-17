FROM python:3
USER root

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install locales \
    libgl1-mesa-dev \
    tesseract-ocr \
    libtesseract-dev \
    && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 学習済みモデルの取得
RUN cd /usr/share/tesseract-ocr/4.00/tessdata/ \
    && wget https://github.com/tesseract-ocr/tessdata/raw/main/jpn.traineddata \
    && wget https://github.com/tesseract-ocr/tessdata_best/raw/main/jpn.traineddata -O best_jpn.traineddata\
    && wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/jpn.traineddata -O fast_jpn.traineddata \
    && wget https://github.com/tesseract-ocr/tessdata/raw/main/jpn_vert.traineddata \
    && wget https://github.com/tesseract-ocr/tessdata_best/raw/main/jpn_vert.traineddata -O best_jpn_vert.traineddata \
    && wget https://github.com/tesseract-ocr/tessdata_fast/raw/main/jpn_vert.traineddata -O fast_jpn_vert.traineddata 


ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir -p /root/src
COPY requirements.txt /root/src
WORKDIR /root/src

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
