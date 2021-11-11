FROM duraark/microservice-base

MAINTAINER Martin Hecher <martin.hecher@fraunhofer.at>

COPY ./ /opt/duraark-geometricenrichment

##
## Build and install 'orthogen'
## FIXXME: 'orthogen' should be used via docker!
##
###RUN mkdir -p /opt/orthogen/build
###COPY ./orthogen /opt/orthogen

###WORKDIR /opt/orthogen/build

###RUN cmake -DEIGEN3_INCLUDE_DIR=/usr/include/eigen3 ../ && make -j2
###RUN cp /opt/orthogen/build/orthogen /usr/local/bin

## Install OpenCV
###RUN apt-get install wget unzip -y && add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) multiverse"
###RUN apt-get update -y
## FIXXME: download from sourceforge is not working ...
##RUN (cd /opt/duraark-geometricenrichment/scripts/Install-OpenCV/Ubuntu && ./opencv_latest.sh)

## Instructions from: http://rodrigoberriel.com/2014/10/installing-opencv-3-0-0-on-ubuntu-14-04/
###RUN mkdir /tmp/opencv && cd /tmp/opencv && wget https://github.com/Itseez/opencv/archive/3.0.0.zip -O /tmp/opencv/opencv-3.0.0.zip && unzip opencv-3.0.0.zip && mkdir /tmp/opencv/opencv-3.0.0/build
###WORKDIR /tmp/opencv/opencv-3.0.0/build
###RUN cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D ITH_TBB=OFF -D WITH_V4L=OFF -D WITH_QT=OFF ../
###RUN make -j $(nproc)
###RUN make install

###RUN mkdir -p /opt/elecdetect/build
###COPY ./elecdetect /opt/elecdetect

###WORKDIR /opt/elecdetect/build
###RUN cmake ../ && make -j6
###RUN cp /opt/elecdetect/build/bin/ElecDetec /usr/local/bin

##
## Install microservice:
##
WORKDIR /opt/duraark-geometricenrichment/src

RUN npm install

EXPOSE 5014

CMD ["/opt/duraark-geometricenrichment/scripts/startAPI.sh"]
