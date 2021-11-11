# Don't edit this file directly, since it was generated from a template,
# and you're changes will be *clobbered*.  Edit the template instead.


FROM matthieudelaro/caffe-ready-ubuntu-pip:latest
# FROM matthieudelaro/mnist-ready:latest

ENV CAFFE_ROOT /opt/caffe
ENV PATH $CAFFE_ROOT/tools:$PATH

RUN pip install scikit-learn>=0.14.1  # dependency of caffe which is really long to build
RUN apt-get install nano -y  # because no, vim is not installed, and yes, I am lost in vi

# Clone the Caffe repo
RUN cd /opt && git clone https://github.com/matthieudelaro/caffe $CAFFE_ROOT
# COPY caffeIUFversion $CAFFE_ROOT

# Install python deps
RUN cd $CAFFE_ROOT && \
  cat python/requirements.txt | xargs -L 1 sudo pip install

# # Build Caffe core
RUN cd $CAFFE_ROOT && \
  cp Makefile.config.example Makefile.config && \
   \
  echo "CXX := /usr/bin/g++-4.6" >> Makefile.config && \
  sed -i 's/CXX :=/CXX ?=/' Makefile

RUN cd $CAFFE_ROOT && \
  # mkdir build && \
  # cd build && \
  # cmake .. && \
  # cmake . && \
  make all -j8

# Add ld-so.conf so it can find libcaffe.so
# ADD caffe-ld-so.conf /etc/ld.so.conf.d/
RUN echo "$CAFFE_ROOT/.build_release/lib/" >> /etc/ld.so.conf.d/caffe-ld-so.conf

# Run ldconfig again (not sure if needed)
RUN ldconfig

# Numpy include path hack - github.com/BVLC/caffe/wiki/Ubuntu-14.04-VirtualBox-VM
RUN ln -s /usr/include/python2.7/ /usr/local/include/python2.7 && \
  ln -s /usr/local/lib/python2.7/dist-packages/numpy/core/include/numpy/ /usr/local/include/python2.7/numpy

# Build Caffe python bindings
RUN cd $CAFFE_ROOT && \
  make python -j8 && \
  make distribute -j8 # no rule for pycaffe :(

RUN echo "run me as following: nvidia-docker run -i -t --device=/dev/nvidia0:/dev/nvidia0 --device=/dev/nvidiactl:/dev/nvidiactl matthieudelaro/caffe-iuf"

