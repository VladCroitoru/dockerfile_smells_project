FROM ubuntu:16.04
MAINTAINER Isac Cavalcante "isaccavalcante@alu.ufc.br"

WORKDIR /app

ADD requirements.txt /app

RUN apt update \
    && apt-get install -y \
    software-properties-common \
    wget \
    curl

RUN add-apt-repository ppa:jonathonf/python-3.6 -y \
    && apt-get update \
    && apt-get install -y \
    python3.6 \
    python3.6-dev 
    
RUN wget https://bootstrap.pypa.io/get-pip.py \
    && python3.6 get-pip.py \
    && ln -s /usr/bin/python3.6 /usr/local/bin/python3

RUN apt-get install -y \
    build-essential \
    qt5-default \
    libqt5webkit5-dev \
    software-properties-common \
    git \
    sox \
    xvfb \
    cmake \
    libjpeg8 \
    libjpeg62-dev \
    libfreetype6 \
    libleptonica-dev \
    libtesseract-dev  \
    imagemagick \
    openvpn \
    zip \
    unzip \
    nano \
    vim \
    pdftohtml \
    locales

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt 

RUN pip3 install dryscrape

RUN git clone https://github.com/isaccavalcante/pyslibtesseract.git \
    && cd pyslibtesseract \
    && cd src/cppcode/ \
    && cmake . \ 
    && make \
    && cd ../.. \
    && python3 setup.py install  

RUN mkdir tessdata \
    && cd tessdata \
    && wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata

RUN locale-gen pt_BR.UTF-8 \
    && update-locale 

ENV TESSDATA_PREFIX="/app"

ENV LANG pt_BR.UTF-8
ENV LC_CTYPE pt_BR.UTF-8
ENV LC_NUMERIC pt_BR.UTF-8
ENV LC_TIME pt_BR.UTF-8
ENV LC_COLLATE pt_BR.UTF-8
ENV LC_MONETARY pt_BR.UTF-8
ENV LC_MESSAGES pt_BR.UTF-8
ENV LC_PAPER pt_BR.UTF-8 
ENV LC_NAME pt_BR.UTF-8 
ENV LC_ADDRESS pt_BR.UTF-8 
ENV LC_TELEPHONE pt_BR.UTF-8 
ENV LC_MEASUREMENT pt_BR.UTF-8 
ENV LC_IDENTIFICATION pt_BR.UTF-8 
