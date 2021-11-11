FROM ubuntu:zesty 

MAINTAINER Uilian Ries <uilianries@gmail.com>

RUN apt-get update -q && apt-get install -y -q clang-3.9 clang-tidy-3.9 clang-format-3.9
RUN ln -s /usr/bin/clang-3.9 /usr/local/bin/clang && ln -s /usr/bin/clang-tidy-3.9 /usr/local/bin/clang-tidy && ln -s /usr/bin/clang-format-3.9 /usr/local/bin/clang-format

RUN groupadd 1001 -g 1001
RUN groupadd 1000 -g 1000
RUN useradd -ms /bin/bash ubuntu -g 1001 -G 1000 && echo "ubuntu:ubuntu" | chpasswd && adduser ubuntu sudo
RUN echo "ubuntu ALL= NOPASSWD: ALL\n" >> /etc/sudoers

USER ubuntu
WORKDIR /home/ubuntu
