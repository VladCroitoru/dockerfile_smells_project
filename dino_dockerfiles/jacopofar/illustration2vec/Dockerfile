FROM ubuntu:wily
#get the repo indexes
RUN apt-get update
# system dependencies needed to install the libraries from pip
#curl is needed because easy_install would fall back to its download method and fail the SSL connection otherwise
#pkg-config is needed to let matplotlib find freetype
RUN apt-get install -y python-setuptools gcc g++ python-dev libhdf5-dev libjpeg-dev zlibc zlib1g-dev libblas-dev liblapack-dev gfortran libfreetype6-dev libpng-dev curl pkg-config
RUN easy_install pip
RUN pip install numpy
RUN pip install scipy
RUN pip install pillow
RUN pip install scikit-image
RUN pip install chainer
RUN apt-get install -y git
RUN git clone https://github.com/rezoo/illustration2vec.git
#wget is necessary to download the models
RUN apt-get install -y wget
RUN cd illustration2vec && ./get_models.sh
WORKDIR /illustration2vec
