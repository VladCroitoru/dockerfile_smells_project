ARG osversion=xenial
FROM ubuntu:${osversion}

ARG VERSION=master
ARG VCS_REF
ARG BUILD_DATE

RUN echo "VCS_REF: "${VCS_REF}", BUILD_DATE: "${BUILD_DATE}", VERSION: "${VERSION}

LABEL maintainer="frank.foerster@ime.fraunhofer.de" \
      description="Dockerfile providing the unicycler software" \
      version=${VERSION} \
      org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.vcs-url="https://github.com/greatfireball/ime_unicycler.git"

RUN apt update && apt install --yes \
      wget \
      build-essential \
      git \
      zlib1g-dev \
      python3-setuptools \
      ncbi-blast+ \
      bowtie2 \
      openjdk-8-jre-headless \
      libncurses5-dev \
      libbz2-dev \
      liblzma-dev \
      python3

WORKDIR /opt
RUN wget -O spades.tar.gz \
        http://cab.spbu.ru/files/release3.13.0/SPAdes-3.13.0-Linux.tar.gz && \
    tar xvzf spades.tar.gz && \
    rm spades.tar.gz
ENV PATH=/opt/SPAdes-3.13.0-Linux/bin/:"$PATH"

WORKDIR /opt
RUN wget -O samtools.tar.bz2 https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2 && \
    tar xjf samtools.tar.bz2 && \
    cd samtools-1.9 && \
    ./configure && \
    make && \
    make check && \
    make install && \
    cd .. && \
    rm -rf samtools-1.9*

WORKDIR /opt
RUN apt install --yes \
        cmake \
        mummer \
	python-numpy \
	python-matplotlib \
	time && \
    wget -O racon.tar.gz https://github.com/isovic/racon/releases/download/1.3.2/racon-v1.3.2.tar.gz && \
    tar xzf racon.tar.gz && \
    cd racon-v1.3.2/ && \
    mkdir build && cd build && \
    cmake -DCMAKE_BUILD_TYPE=Release -Dracon_build_tests=ON .. && \
    make && \
    bin/racon_test && \
    make install && \
    cd /opt && rm -rf racon*

ENV PATH=/opt/racon/bin/:"$PATH"

WORKDIR /opt
RUN mkdir pilon-1.23 && \
    cd pilon-1.23 && \
    wget https://github.com/broadinstitute/pilon/releases/download/v1.23/pilon-1.23.jar && \
    ln -s pilon-1.23.jar pilon.jar && \
    bash -c 'echo -e "#!/bin/bash\njava -Xmx128G -jar /opt/pilon-1.23/pilon.jar $@" > pilon' && \
    chmod +x pilon
ENV PATH=/opt/pilon-1.23/:"$PATH"

ENV PYTHONPATH=/opt/lib/python3.5/site-packages/
ENV PATH=/opt/bin/:"$PATH"
RUN git clone --branch v0.4.7 https://github.com/rrwick/Unicycler.git /opt/unicycler && \
    cd /opt/unicycler && \
    python3 setup.py install --prefix=/opt/

ENTRYPOINT ["unicycler"]

VOLUME /data
WORKDIR /data
