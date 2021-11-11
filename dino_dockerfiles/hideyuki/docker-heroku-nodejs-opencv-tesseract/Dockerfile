# Inherit from Heroku's stack
FROM heroku/nodejs

# Install OpenCV
RUN mkdir -p /app/.heroku/opencv /tmp/opencv
ADD Install-OpenCV /tmp/opencv
WORKDIR /tmp/opencv/Ubuntu
RUN echo 'deb http://archive.ubuntu.com/ubuntu trusty multiverse' >> /etc/apt/sources.list && apt-get update
RUN version=2.4.13 ./opencv_latest.sh

WORKDIR /app/user

# Install leptonica for tesseract
RUN mkdir ~/temp &&\ 
    cd ~/temp/ &&\ 
    wget http://www.leptonica.org/source/leptonica-1.73.tar.gz &&\ 
    tar xvf leptonica-1.73.tar.gz &&\ 
    cd leptonica-1.73 &&\ 
    ./configure &&\ 
    make &&\ 
    checkinstall &&\ 
    ldconfig &&\
    rm -rf ~/temp

# Install tesseract
RUN mkdir ~/temp &&\
    cd ~/temp/ &&\ 
    wget https://github.com/tesseract-ocr/tesseract/archive/3.04.01.tar.gz &&\ 
    tar xvf 3.04.01.tar.gz &&\ 
    cd tesseract-3.04.01 &&\ 
    ./autogen.sh &&\ 
    mkdir ~/local &&\ 
    ./configure --prefix=$HOME/local/ &&\ 
    make &&\ 
    make install &&\ 
    cd ~/ &&\ 
    rm -rf ~/temp

# Add tesseact eng data
RUN cd ~/local/share &&\ 
    wget https://github.com/tesseract-ocr/tessdata/archive/3.04.00.tar.gz &&\ 
    tar xvf 3.04.00.tar.gz &&\
    mkdir -p tesseract-ocr/tessdata &&\
    cp tessdata-3.04.00/eng* tesseract-ocr/tessdata/ &&\
    rm -rf 3.04.00.tar.gz tessdata-3.04.00

ENV PKG_CONFIG_PATH $PKG_CONFIG_PATH:/app/.heroku/opencv/lib/pkgconfig
ENV PATH $PATH:/root/local/bin
ENV TESSDATA_PREFIX /root/local/share/tesseract-ocr/

ONBUILD ADD package.json /app/user/
ONBUILD RUN npm install
ONBUILD ADD . /app/user/

