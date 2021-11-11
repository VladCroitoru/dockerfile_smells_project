# BUILD:        docker build -t bitcoin .
# RUN:          docker run -it --rm -v (command pwd):/home/jochen/src/bitcoin bitcoin /bin/sh
#      aws:     sudo docker run -it --rm -v $PWD:/home/jochen/src/bitcoin -u 500 bitcoin /bin/sh
#
# aws:
#    sudo docker run -dt --name btc -v /home/ec2-user/src/bitcoin:/home/jochen/src/bitcoin -u 500 gin66/bc_base /bin/bash
#    sudo docker exec -it btc /usr/bin/tmux 
#       => ./start.sh
#    sudo docker exec -it btc /usr/bin/tmux attach 
#
# runtime on docker hub: >19 minutes
#
#===========================================================================
# This is from official docker python Dockerfile
FROM alpine:3.6

# not part of official Dockerfile
RUN apk update && apk upgrade

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# install ca-certificates so that HTTPS works consistently
# the other runtime dependencies for Python are installed later
RUN apk add --no-cache ca-certificates

RUN apk add --no-cache --virtual .fetch-deps \
		gnupg \
		openssl \
		tar \
		xz

RUN apk add --no-cache --virtual .build-deps  \
		bzip2-dev \
		gcc \
		gdbm-dev \
		libc-dev \
		linux-headers \
		make \
		ncurses-dev \
		openssl \
		openssl-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		xz-dev \
		zlib-dev

# the lapack package is only in the community repository
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk add --no-cache curl tmux nodejs git fish vim bash memcached less sqlite \
                       llvm clang make gcc automake gfortran musl-dev g++ \
                       lapack-dev freetype-dev mdocml-apropos \
                       man man-pages jpeg-dev python3 python3-dev
            
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN pip3 install --upgrade setuptools
RUN pip3 install six requests websocket-client requests-futures pusherclient socketio_client pymemcache \
                 numpy python-telegram-bot pypng scipy ipython pika amqpstorm pillow 
RUN pip3 install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.1.0-cp36-cp36m-linux_x86_64.whl
RUN pip3 install tflearn
#h5py

RUN /usr/sbin/adduser -u 500 -D ec2-user
RUN /usr/sbin/adduser -u 1000 -D jochen
RUN /usr/sbin/adduser -u 5000 -D jo88ki88
#USER jochen
#WORKDIR /home/jochen/src/bitcoin

# on ec2 is uid 500
#USER ec2-user
#WORKDIR /home/ec2-user/src/prob_logic
