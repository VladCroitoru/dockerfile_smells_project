FROM ubuntu:rolling

RUN apt-get update &&\
  DEBIAN_FRONTEND=noninteractive apt-get install -qy libterm-readline-gnu-perl &&\
  DEBIAN_FRONTEND=noninteractive apt-get install -qy strace curl procps less man &&\
  apt-get clean -y && rm -rf /var/lib/apt/lists/*

