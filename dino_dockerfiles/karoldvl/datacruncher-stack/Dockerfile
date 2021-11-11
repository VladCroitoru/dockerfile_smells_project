FROM jupyter/datascience-notebook:28515ed64e5e

MAINTAINER Karol Piczak <karol@dvl.pl>

ENV DATACRUNCHER_VERSION=2016-10-11


USER root

RUN apt-get update && apt-get install -y \
  build-essential \
  g++ \
  git \
  less \
  libav-tools \
  libffi-dev \
  libgeos++ \
  libopenblas-dev \
  libopencv-dev \
  libsamplerate0 \
  libsamplerate0-dev \
  libsndfile-dev \
  libsndfile1 \
  libssl-dev \
  module-init-tools \
  portaudio19-dev \
  python-opencv \
  sox \
  subversion \
  tmux \
  unzip \
  wget

# GPU support
RUN cd /opt && \
  wget --no-verbose https://developer.nvidia.com/compute/cuda/8.0/prod/local_installers/cuda_8.0.44_linux-run && \
  mkdir nvidia_installers && \
  chmod +x cuda_8.0.44_linux-run && \
  ./cuda_8.0.44_linux-run --extract=`pwd`/nvidia_installers && \
  cd nvidia_installers && \
  ./NVIDIA-Linux-x86_64-367.48.run -s -N --no-kernel-module && \
  ./cuda-linux64-rel-8.0.44-21122537.run -noprompt && \
  rm -f ../cuda_8.0.44_linux-run && \
  rm -f *.run

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-8.0/lib64
ENV PATH=$PATH:/usr/local/cuda-8.0/bin
RUN ldconfig

# Conda updates
RUN printf "[samplerate]\nlibrary_dirs=/usr/lib/x86_64-linux-gnu/\ninclude_dirs=/usr/include/" >> ~/.numpy-site.cfg && \
  printf "\n[sndfile]\nlibrary_dirs=/usr/lib/x86_64-linux-gnu/\ninclude_dirs=/usr/include/" >> ~/.numpy-site.cfg

RUN conda update --quiet \
  bokeh \
  h5py \
  scikit-image \
  scikit-learn
RUN conda install --quiet libgfortran

# Custom font
RUN cd /usr/share/fonts && \
  wget --no-verbose "https://github.com/google/fonts/raw/master/ofl/ptsans/PT_Sans-Web-Regular.ttf" && \
  fc-cache -fv && \
  rm -f /root/.cache/matplotlib/fontList*


USER jovyan

# Install Python3 packages
RUN pip install --upgrade -I setuptools

RUN pip install \
  boto \
  coverage==3.7.1 \
  descartes \
  GitPython \
  googlemaps \
  graphviz \ 
  ipdb \
  https://github.com/ipython-contrib/IPython-notebook-extensions/archive/master.zip \
  ipywidgets \
  joblib \
  librosa \
  line_profiler \
  mem_top \
  memory_profiler \
  msgpack-python \
  nose \
  objgraph \
  openpyxl \
  pep8 \
  prettyplotlib \
  psutil \
  PyAudio==0.2.8 \
  pycallgraph \
  https://github.com/karoldvl/fork-pydub/archive/quick-fix.zip \
  pympler \
  pysal \
  pytest \
  pytest-cov \
  pytest-pep8 \
  pytest-xdist \
  python-coveralls \
  PyYAML \
  quandl \
  scikit-image \
  scikits.audiolab==0.11.0 \
  scikits.bootstrap \
  scikits.samplerate==0.3.3 \
  git+git://github.com/mwaskom/seaborn.git \
  git+git://github.com/TUT-ARG/sed_eval.git \
  git+git://github.com/TUT-ARG/sed_vis.git \
  tqdm \
  wavefile==1.3
  
# Theano
ENV THEANO_FLAGS=floatX=float32,device=gpu0
RUN cd /home/jovyan && \
  git clone git://github.com/Theano/Theano.git && \
  cd /home/jovyan/Theano && \
  /opt/conda/bin/python setup.py develop

# pylearn2
RUN cd /home/jovyan && \
  git clone git://github.com/lisa-lab/pylearn2.git && \
  cd /home/jovyan/pylearn2 && \
  /opt/conda/bin/python setup.py develop
ENV PYLEARN2_DATA_PATH=/opt/data

# TensorFlow
RUN pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0-cp35-cp35m-linux_x86_64.whl

# Keras
RUN pip install git+git://github.com/fchollet/keras.git

# Final setup
RUN mkdir -p /home/jovyan/.local/share/jupyter && \
  ln -s /key.pem /home/jovyan/.local/share/jupyter/notebook.pem && \
  chown -R jovyan:users /home/jovyan/.local

# Generate font cache
RUN /opt/conda/bin/ipython -c 'import matplotlib.pyplot'
  
