FROM ubuntu:latest

RUN apt-get -q update -y && apt-get -qq install -y \
sudo \
cmake cmake-data \
libopenmpi-dev openmpi-bin \
libboost-all-dev \
liblapack-dev liblapacke-dev \
python2.7 python-pip git \
wget curl lcov doxygen \
ccache texlive-latex-base texlive-fonts-recommended texlive-latex-recommended texlive-font-utils \
g++ gfortran


RUN groupadd -r portage
RUN useradd -r -m -g portage -G sudo portage
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER portage
ENV PATH=/usr/lib/ccache:${PATH}
WORKDIR /home/portage
RUN pip install --user codecov coverxygen
