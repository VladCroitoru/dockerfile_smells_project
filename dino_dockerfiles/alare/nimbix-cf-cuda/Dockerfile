FROM nimbix/ubuntu-cuda

RUN sudo apt-get -y update
RUN sudo apt-get install -y software-properties-common
RUN sudo add-apt-repository -y ppa:george-edison55/cmake-3.x
RUN sudo apt-get -y update
RUN sudo apt-get install -y cmake
RUN sudo apt-get install -y doxygen
RUN sudo apt-get install -y openssl libssl-dev lcov

RUN wget -nc https://github.com/google/protobuf/archive/v3.0.2.tar.gz
RUN wget -nc https://github.com/protobuf-c/protobuf-c/archive/v1.2.1.tar.gz
RUN wget -nc https://developer.nvidia.com/compute/cuda/8.0/prod/local_installers/cuda-repo-ubuntu1604-8-0-local_8.0.44-1_amd64-deb -O cuda.deb


RUN echo "Version 4" > ~/Version

ADD ./NAE/help.html /etc/NAE/help.html

CMD /bin/bash
