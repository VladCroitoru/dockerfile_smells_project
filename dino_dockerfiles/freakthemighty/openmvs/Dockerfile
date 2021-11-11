FROM ubuntu:14.04

# Fetch dependencies from apt-get
RUN apt-get update && apt-get install -y \
  cmake \ 
  graphviz \
  git \ 
  libatlas-base-dev \ 
  libboost-all-dev \ 
  libcgal-dev \
  libeigen3-dev \ 
  libgoogle-glog-dev \
  libjpeg-dev \ 
  libopencv-dev \
  libpng-dev \ 
  libsuitesparse-dev \ 
  libtiff-dev \ 
  libxi-dev  \ 
  libxrandr-dev \ 
  libxxf86vm-dev \ 
  libxxf86vm1

# Install Ceres
RUN git clone https://ceres-solver.googlesource.com/ceres-solver && \
  mkdir ceres_Build && \
  cd ceres_Build/ && \
  cmake . ../ceres-solver/ && \
  make && \
  make install && \
  cd ..

# Install VCG
RUN cd /opt && git clone https://github.com/cdcseacave/VCG.git vcglib

#OpenMVG build
RUN cd /opt && \
  git clone --recursive https://github.com/openMVG/openMVG.git && \ 
  mkdir openMVG_Build && \
  cd openMVG_Build && \
  cmake -DCMAKE_BUILD_TYPE=RELEASE . ../openMVG/src/ -DCMAKE_INSTALL_PREFIX=/opt/openMVG_install && \
  make install


ADD . /opt/openMVS

# Patch VCG
RUN cp /opt/openMVS/build/clean.patch /opt/vcglib/vcg/complex/algorithms && \
  cd /opt/vcglib/vcg/complex/algorithms && \
  patch < clean.patch

#OpenMVS build
RUN ln -s /usr/lib/x86_64-linux-gnu/libGLU.so.1.3.1 /usr/lib/x86_64-linux-gnu/libGLU.so && \ 
  ln -s /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1  /usr/lib/x86_64-linux-gnu/libGL.so && \ 
  mkdir /opt/openMVS_Build && \
  cd /opt/openMVS_Build && \
  cmake . ../openMVS -DCMAKE_BUILD_TYPE=RELEASE -DVCG_DIR="/opt/vcglib" -DCERES_DIR="/usr/local/share/Ceres" -DOpenCV_CAN_BREAK_BINARY_COMPATIBILITY=OFF -DOpenMVG_DIR:STRING="/opt/openMVG_install/share/openMVG/cmake/" && \
  make && \
  cp ./bin/* /usr/bin
