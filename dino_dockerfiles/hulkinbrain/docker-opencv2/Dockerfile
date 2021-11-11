FROM python:2
MAINTAINER hulkibrain <alevoorsoorya01@gmail.com>

# Installing dependencies for linux installation of opencv
RUN apt-get update && \
        apt-get install -y \
        build-essential \
        cmake \
        git \
        wget \
        unzip \
        yasm \
        pkg-config \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libjpeg-dev \
        libpng-dev \
        libtiff-dev \
        libjasper-dev \
        libavformat-dev \
        libpq-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# GUI (if you want to use GTK instead of Qt, replace 'qt5-default' with 'libgtkglext1-dev' and remove '-DWITH_QT=ON' option in CMake):

RUN wget https://github.com/opencv/opencv/archive/2.4.13.3.zip \
&& unzip 2.4.13.3.zip \
&& mkdir /opencv-2.4.13.3/cmake_binary \
&& cd /opencv-2.4.13.3/cmake_binary \
&& cmake -DWITH_QT=OFF \
        -DWITH_OPENGL=ON \
        -DFORCE_VTK=OFF \
        -DWITH_TBB=ON \
        -DWITH_GDAL=ON \
        -DWITH_XINE=ON \
        -DBUILD_EXAMPLES=OFF \
        -DENABLE_PRECOMPILED_HEADERS=OFF .. \
&& make install \
&& rm /2.4.13.3.zip \
&& rm -r /opencv-2.4.13.3

# Run the image as a non-root user
RUN adduser myuser
USER myuser

# Add your project repository
# SYNTAX -->   ADD ./yourFolder /someFolder/youFolder
# The "/someFolder/youFolder" name could be anything, in this example it is /opt/app
# It could simply be /app or /wookie/chewbacca or anything, change following commands accordingly

ADD ./app /opt/app/
WORKDIR /opt/app

# Running a test file
# Do project related stuff here

CMD python test.py
