FROM python:latest
MAINTAINER Andis Cirulis "andis.cirulis@whitedigital.eu"

#ENV PYTHONUNBUFFERED 1

#RUN apt-get install -y tk-dev python3-tk
#RUN apt-get install -y python3-pyqt5
# RUN pip install pyqt5

RUN apt-get -y update \
&& apt-get -y upgrade \
&& apt-get -y dist-upgrade \
&& apt-get -y autoremove \
&& apt-get install -y vim apt-utils

WORKDIR /root
COPY  requirements.txt /root/
RUN pip3 install -r requirements.txt

#lets wait for matplotlib 2.0.1 before this will fixed
# ENV MPLBACKEND TkAgg

#lets install yolo
RUN git clone https://github.com/pjreddie/darknet \
&& cd darknet \
&& make

ENV PATH $PATH:/root/darknet

#lets install opencv
# RUN apt-get install -y build-essential python3-dev python-dev cmake unzip wget qt5-default libvtk6-dev libjpeg62-turbo-dev libtiff5-dev libjasper-dev libpng12-dev\
# && wget https://github.com/opencv/opencv/archive/3.2.0.zip

# RUN unzip 3.2.0.zip \
# && rm 3.2.0.zip \
# && mv opencv-3.2.0 OpenCV \
# && cd OpenCV \
# && mkdir build \
# && cd build \
# && cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON -DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON -DENABLE_PRECOMPILED_HEADERS=OFF .. \
# && make -j4 \
# && make install \
# && ldconfig


ENTRYPOINT  ["bash"]
