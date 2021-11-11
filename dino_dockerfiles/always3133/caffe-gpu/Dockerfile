FROM always3133/ubuntu-cuda4tesla

# Get dependencies
RUN apt-get update && apt-get install -y \
  libprotobuf-dev \
  libleveldb-dev \
  libsnappy-dev \
  libopencv-dev \
  libboost-all-dev \ 
  libhdf5-serial-dev \ 
  protobuf-compiler \ 
  gcc-4.8 \ 
  g++-4.8 \ 
  gcc-4.8-multilib \  
  g++-4.8-multilib \ 
  gfortran \ 
  libjpeg62 \ 
  libfreeimage-dev \  
  libatlas-base-dev \  
  libopenblas-dev \
  git \ 
  bc \ 
  wget \ 
  curl \ 
  unzip \ 
  cmake \ 
  liblmdb-dev \  
  pkgconf

# Use gcc 4.8
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.8 30 && \
  update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.8 30 && \ 
  update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 30 && \
  update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 30

# Clone the Caffe repo 
RUN cd /opt && git clone https://github.com/nakosung/caffe.git && (cd caffe; git checkout dqn)

# Glog 
RUN cd /opt && wget https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz && \
  tar zxvf glog-0.3.3.tar.gz && \
  cd /opt/glog-0.3.3 && \
  ./configure && \
  make && \
  make install

# Workaround for error loading libglog: 
#   error while loading shared libraries: libglog.so.0: cannot open shared object file
# The system already has /usr/local/lib listed in /etc/ld.so.conf.d/libc.conf, so
# running `ldconfig` fixes the problem (which is simpler than using $LD_LIBRARY_PATH)
# TODO: looks like this needs to be run _every_ time a new docker instance is run,
#       so maybe LD_LIBRARY_PATh is a better approach (or add call to ldconfig in ~/.bashrc)
RUN ldconfig

# Gflags
RUN cd /opt && \
  wget https://github.com/schuhschuh/gflags/archive/master.zip && \
  unzip master.zip && \
  cd /opt/gflags-master && \
  mkdir build && \
  cd /opt/gflags-master/build && \
  export CXXFLAGS="-fPIC" && \
  cmake .. && \ 
  make VERBOSE=1 && \
  make && \
  make install

# Build Caffe core
RUN cd /opt/caffe && cp Makefile.config.example Makefile.config
RUN cd /opt/caffe && echo "CXX := /usr/bin/g++-4.8" >> Makefile.config 
RUN cd /opt/caffe && sed -i 's/atlas/open/' Makefile.config
RUN cd /opt/caffe && sed -i 's/CXX :=/CXX ?=/' Makefile
RUN cd /opt/caffe && make all
