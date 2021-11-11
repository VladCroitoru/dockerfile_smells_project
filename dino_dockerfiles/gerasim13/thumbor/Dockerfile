FROM phusion/baseimage
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

COPY requirements.txt /tmp/

RUN apt-get update	
RUN apt-get install -y --no-install-recommends git curl libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
RUN apt-get install -y --no-install-recommends python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libgif-dev libjasper-dev libdc1394-22-dev
RUN apt-get install -y --no-install-recommends libgraphicsmagick++1-dev libboost-python-dev libcurl4-openssl-dev
RUN apt-get install -y --no-install-recommends libpng3 libtiff5 libjasper1 libjpeg62 libjpeg8-dev libjpeg-turbo8 libjpeg-turbo8-dev libdc1394-22 libdc1394-utils
RUN apt-get install -y --no-install-recommends webp python-pycurl python-pip python2.7-dev python3.4-dev gifsicle
RUN apt-get install -y --no-install-recommends python-opencv
RUN apt-get install -y --no-install-recommends build-essential
RUN apt-get -y autoremove

# RUN apt-get install -y --no-install-recommends cmake
# RUN mkdir ~/opencv && cd ~/opencv
# RUN git clone https://github.com/Itseez/opencv.git ~/opencv
# RUN mkdir ~/opencv/release && cd ~/opencv/release && \
# 	cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local \
# 		  -D BUILD_PYTHON_SUPPORT=ON -D WITH_XINE=ON -D WITH_TBB=ON \
# 		  -D WITH_JPEG=ON .. && \
# 		  make && make install
# RUN export PYTHONPATH=$PYTHONPATH:/usr/lib/pymodules/python2.7/
# RUN export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages
# RUN export PYTHONPATH=$PYTHONPATH:/usr/lib/pyshared/python2.7/
# RUN export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages/
# RUN rm -rf ~/opencv

RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
RUN rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
EXPOSE 8888

ENTRYPOINT ["thumbor"]
CMD ["-p 8888"]
