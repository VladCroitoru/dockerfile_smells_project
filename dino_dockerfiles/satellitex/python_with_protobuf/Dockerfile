FROM ubuntu:16.10

RUN apt-get update && apt-get -y upgrade && \
    apt-get -y install python3-pip \
    wget curl unzip dh-autoreconf && apt-get -y clean

# python3.6
RUN apt -y install python3.6-dev python3.6-venv; \
    wget https://bootstrap.pypa.io/get-pip.py; \
    python3.6 get-pip.py; \
    ln -s /usr/bin/python3.6 /usr/local/bin/python3; \
    ln -s /usr/local/bin/pip /usr/local/bin/pip3; \
    # use python3 as default
    ln -s /usr/bin/python3.6 /usr/local/bin/python;

# install protobuf 3.3.2
WORKDIR /tmp
RUN wget https://github.com/google/protobuf/archive/v3.3.2.tar.gz; \
    tar -zxvf v3.3.2.tar.gz

WORKDIR /tmp/protobuf-3.3.2
RUN ./autogen.sh && ./configure && make install && ldconfig; \
    rm /tmp/v3.3.2.tar.gz

CMD ["/bin/bash"]
