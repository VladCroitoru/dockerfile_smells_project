FROM 32bit/ubuntu:16.04

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y flex bison build-essential csh openjdk-8-jdk \
       libxaw7-dev wget \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/class \
    && cd /usr/class \
    && wget http://spark-university.s3.amazonaws.com/stanford-compilers/vm/student-dist.tar.gz \
    && tar -xf student-dist.tar.gz \
    && rm student-dist.tar.gz

ENV PATH=/usr/class/cs143/cool/bin:$PATH

RUN mkdir /workspace
WORKDIR /workspace

# Don't use symbolic links
RUN sed -i -e 's/ln -s/cp -r -L/g' /usr/class/cs143/assignments/*/Makefile
