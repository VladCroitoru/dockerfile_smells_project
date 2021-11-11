FROM qnib/alpn-infiniband

ADD hello_mpi.c /usr/local/src/
RUN apk update && apk upgrade \
 && apk add vim wget tar gcc g++ make libgcrypt-dev perl unzip flex autoconf automake libtool build-base \
 && wget -qO /tmp/openmpi.zip https://github.com/open-mpi/ompi/archive/master.zip \
 && cd /opt/ \
 && unzip -q /tmp/openmpi.zip 
RUN cd /opt/ompi-master \
 && ./autogen.pl \ 
 && sh ./configure --enable-orterun-prefix-by-default \
 && make -j4 && make install \
 && mpicc -o /usr/local/bin/hello_mpi /usr/local/src/hello_mpi.c \
 && apk del g++ make perl tar gcc wget libgcrypt-dev libtool automake autoconf flex unzip \
 && rm -rf /var/cache/apk/*
