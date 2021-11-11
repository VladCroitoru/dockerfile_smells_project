FROM ubuntu
MAINTAINER Justin Murray <murrayju@gmail.com>
CMD ["bash"]

RUN apt-get update && apt-get install -y ssh git vim editorconfig python python3
RUN locale-gen en_US.utf8
ENV SHELL /bin/bash
COPY [".", "/root/.dotfiles"]
WORKDIR /root/.dotfiles
RUN bash -ex bootstrap.sh -f
WORKDIR /
