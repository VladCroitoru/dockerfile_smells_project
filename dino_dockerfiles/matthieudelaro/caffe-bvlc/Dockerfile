# Don't edit this file directly, since it was generated from a template,
# and you're changes will be *clobbered*.  Edit the template instead.

# inspired by tleyden5iwx/caffe-gpu-master

FROM matthieudelaro/caffe-ready-ubuntu-pip:latest

# Clone the Caffe repo
RUN cd /opt && git clone https://github.com/BVLC/caffe.git

# Install python deps
RUN cd /opt/caffe && \
  cat python/requirements.txt | xargs -L 1 sudo pip install

# # Build Caffe core
RUN cd /opt/caffe && \
  cp Makefile.config.example Makefile.config && \
   \ 
  echo "CXX := /usr/bin/g++-4.6" >> Makefile.config && \
  sed -i 's/CXX :=/CXX ?=/' Makefile && \
  make all -j8

# Add ld-so.conf so it can find libcaffe.so
# ADD caffe-ld-so.conf /etc/ld.so.conf.d/
RUN echo "/opt/caffe/.build_release/lib/" >> /etc/ld.so.conf.d/caffe-ld-so.conf 

# Run ldconfig again (not sure if needed)
RUN ldconfig

# Numpy include path hack - github.com/BVLC/caffe/wiki/Ubuntu-14.04-VirtualBox-VM
RUN ln -s /usr/include/python2.7/ /usr/local/include/python2.7 && \
  ln -s /usr/local/lib/python2.7/dist-packages/numpy/core/include/numpy/ /usr/local/include/python2.7/numpy

# Build Caffe python bindings
RUN cd /opt/caffe && make pycaffe -j8

ENV CAFFE_ROOT /opt/caffe
ENV PATH $CAFFE_ROOT/build/tools:$PATH
