FROM ubuntu:14.04

# Install OpenCV 3.0
RUN apt-get -y update
RUN apt-get -y install python-pip git nano curl tmux htop mc wget libeigen3-dev
RUN apt-get install -y build-essential cmake libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev ocl-icd-opencl-dev libcanberra-gtk3-module
RUN pip install matplotlib

RUN git clone https://github.com/Itseez/opencv.git

RUN mkdir /opencv/build
WORKDIR /opencv/build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D BUILD_PYTHON_SUPPORT=ON \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D WITH_OPENGL=ON \
      -D WITH_TBB=OFF \
      -D BUILD_EXAMPLES=ON \
      -D BUILD_NEW_PYTHON_SUPPORT=ON \
      -D WITH_V4L=ON \
      ..
RUN make -j7
RUN make install

# Install Node.js
RUN \
  cd /tmp && \
  wget http://nodejs.org/dist/node-latest.tar.gz && \
  tar xvzf node-latest.tar.gz && \
  rm -f node-latest.tar.gz && \
  cd node-v* && \
  ./configure && \
  CXX="g++ -Wno-unused-local-typedefs" make && \
  CXX="g++ -Wno-unused-local-typedefs" make install && \
  cd /tmp && \
  rm -rf /tmp/node-v* && \
  npm install -g npm && \
  echo -e '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc

RUN ldconfig

# Define default command.
CMD ["bash"]
