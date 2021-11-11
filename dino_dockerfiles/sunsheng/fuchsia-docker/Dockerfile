FROM ubuntu:trusty

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y make unrar-free autoconf automake libtool gcc g++ gperf \
    flex bison texinfo gawk ncurses-dev libexpat-dev python-dev python python-serial \
    sed unzip bash help2man wget bzip2

RUN sudo apt-get -y install golang git-all build-essential curl


RUN curl -s https://raw.githubusercontent.com/fuchsia-mirror/jiri/master/scripts/bootstrap_jiri | bash -s fuchsia

WORKDIR fuchsia

RUN cp .jiri_root/bin/jiri /usr/local/bin
RUN chmod 755 /usr/local/bin/jiri

# RUN pwd
# ENV TMP $(pwd)
# ENV PATH=/fuchsia/.jiri_root/bin:${PATH}
# RUN echo $PATH

RUN jiri import fuchsia https://fuchsia.googlesource.com/manifest

RUN jiri update -v
