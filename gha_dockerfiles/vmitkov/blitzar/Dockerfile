# our local base image
FROM ubuntu:focal

LABEL description="Container for use with Visual Studio" 

# install build dependencies 
RUN apt-get update && apt-get install -y gcc g++ \
	cmake make ninja-build rsync zip openssh-server gdb

# if CC is null, set it to 'gcc' (or leave as is otherwise).
ENV CC=${CC:-"gcc"}
ENV CXX=${CXX:-"g++"}

RUN wget -O boost_1_77_0.tar.gz http://sourceforge.net/projects/boost/files/boost/1.77.0/boost_1_77_0.tar.gz/download && \
	tar xzf boost_1_77_0.tar.gz && \
	cd boost_1_77_0 && \
	./bootstrap.sh --prefix=/usr/local --with-libraries=system,thread,test && \
	./b2 link=shared threading=multi variant=release && \
	./b2 install && \
	cd ../

# configure SSH for communication with Visual Studio 
RUN mkdir -p /var/run/sshd

RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \ 
   ssh-keygen -A 

# expose port 22 
EXPOSE 22

ENTRYPOINT service ssh restart && bash

RUN useradd -m -d /home/user -s /bin/bash -G sudo user
RUN echo 'user:resu' | chpasswd
