FROM ubuntu:15.10
RUN apt-get update && apt-get install -y openjdk-8-jdk pkg-config zip g++ zlib1g-dev unzip
RUN mkdir /src
WORKDIR /src

RUN apt-get install -y swig python-pip git python-numpy bash-completion curl

RUN curl -OL https://github.com/bazelbuild/bazel/releases/download/0.2.2/bazel-0.2.2-installer-linux-x86_64.sh
RUN chmod +x bazel-0.2.2-installer-linux-x86_64.sh
RUN ./bazel-0.2.2-installer-linux-x86_64.sh
RUN export PATH="$PATH:$HOME/bin"

RUN pip install -U protobuf==3.0.0b2
RUN pip install asciitree

RUN git clone --recursive https://github.com/tensorflow/models.git
WORKDIR /src/models/syntaxnet/tensorflow
RUN echo "/usr/bin/python" | ./configure
WORKDIR /src/models/syntaxnet
# RUN bazel test syntaxnet/... util/utf8/...