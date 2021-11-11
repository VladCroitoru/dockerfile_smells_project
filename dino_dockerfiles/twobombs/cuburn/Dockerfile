FROM twobombs/deploy-nvidia-docker

# add build tools
RUN apt-get update&&apt-get install -y git software-properties-common python-setuptools python3-setuptools python-migrate && apt-get clean all
RUN add-apt-repository universe && apt-get update && export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y ant libboost-all-dev python-pycuda python-pip && apt-get clean all

# add dependancies & viewers
RUN git clone --recursive https://github.com/stevenrobertson/cuburn.git
RUN git clone --recursive https://github.com/mebigfatguy/apophysis-j.git
RUN cd /apophysis-j && ant 
RUN add-apt-repository ppa:paulo-miguel-dias/mesa -y && pip install numpy scipy && apt-get clean all
