FROM nefrock/docker-ai-base-gpu:latest
MAINTAINER siwazaki@nefrock.com

RUN apt-get update && apt-get install -y emacs zsh libmysqlclient-dev vim
RUN pip3 install --force-reinstall --upgrade pip
RUN pip3 install -U setuptools

RUN pip3 --no-cache-dir install \
  moviepy \
  sklearn \
  msgpack-python \
  tqdm \
  wget \
  sh \
  colorama \
  Pillow \
  wheel \
  pandas \
  jupyter


ENV PATH $PATH:/usr/local/nvidia/bin
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH

RUN pip3 install --upgrade --no-deps git+git://github.com/Theano/Theano.git
RUN echo "[global]\ndevice=gpu\nfloatX=float32\noptimizer_including=cudnn\n[nvcc]\nfastmath=True" > /root/.theanorc

RUN pip3 install tensorflow-gpu==1.2.0

RUN pip3 install pyzmq --install-option="--zmq=bundled"
RUN pip3 install msgpack-python seaborn tqdm wget sh colorama
RUN pip3 install chainer==2.0.0
RUN pip3 install keras==2.0.5