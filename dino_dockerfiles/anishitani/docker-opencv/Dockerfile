FROM python:3-alpine

ENV OPENCV_VERSION 3.2.0

# Install compilation packages
RUN apk add --update gcc g++ make cmake wget unzip

RUN mkdir /tmp/opencv \
    && cd /tmp/opencv \
    && wget -q https://github.com/opencv/opencv/archive/$OPENCV_VERSION.zip \
    && unzip $OPENCV_VERSION.zip \
    && rm $OPENCV_VERSION.zip \
    && mkdir build \
    && cd build \
    && cmake ../opencv-$OPENCV_VERSION \
    && make -j4 \
    && make install \
    && cd / \
    && rm /tmp/opencv
