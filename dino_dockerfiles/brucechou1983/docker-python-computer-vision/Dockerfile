FROM ubuntu:trusty

MAINTAINER brucechou1983 <brucechou1983@gmail.com>

# Install system dependencies
RUN apt-get update
RUN apt-get install -y build-essential wget tar
RUN apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
RUN apt-get install -y python-setuptools python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

# mount folders
ADD . /app

# workdir
WORKDIR /app

# Build opencv (2.4.13.2)
RUN wget https://github.com/opencv/opencv/archive/2.4.13.2.tar.gz && tar xf 2.4.13.2.tar.gz && cd opencv-2.4.13.2 && mkdir release && cd release && \
cmake -DCMAKE_BUILD_TYPE=RELEASE \
-DCMAKE_INSTALL_PREFIX=/usr/local \
-DPYTHON2_EXECUTABLE=/usr/local/bin/python2.7 \
-DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
-DPYTHON_INCLUDE_DIR2=/usr/include/x86_64-linux-gnu/python2.7 \
-DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython2.7.so \
-DPYTHON2_NUMPY_INCLUDE_DIRS=/usr/lib/python2.7/dist-packages/numpy/core/include/ \
-DINSTALL_PYTHON_EXAMPLES=ON \
-DBUILD_NEW_PYTHON_SUPPORT=ON .. \
&& make -j4 && make install \
RUN rm 2.4.13.2.tar.gz \
RUN rm -rf opencv-2.4.13.2

# Fix cv2 import warning
RUN ln /dev/null /dev/raw1394

# Install python dependencies
RUN easy_install pip
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# ports
EXPOSE 7000

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

# Run jupyter notebook
CMD ["jupyter", "notebook", "--port=7000", "--no-browser", "--ip=0.0.0.0", "--NotebookApp.token=\"\"", "--NotebookApp.disable_check_xsrf=True"]
