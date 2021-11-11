FROM ubuntu:latest

RUN apt update \
  && apt install -y curl git vim gnupg python3.8 python3.8-distutils\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3.8 python

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python get-pip.py \
  && rm get-pip.py

RUN pip install numpy notebook matplotlib

RUN curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg
RUN mv bazel.gpg /etc/apt/trusted.gpg.d/
RUN echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list

RUN apt update \
  && apt install -y bazel

WORKDIR /nn

CMD /bin/bash
