FROM ubuntu:latest

LABEL maintainer "user"

ENV USER user
ENV HOME /home/${USER}
ENV SHELL /bin/bash

RUN useradd -m ${USER}
RUN gpasswd -a ${USER} sudo
RUN echo "${USER}:work" | chpasswd
SHELL ["/bin/bash", "-c"]

RUN dpkg-divert --local --rename --add /sbin/initctl
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y
RUN apt-get install -y git sudo curl gcc make

RUN curl -O https://dl.google.com/go/go1.17.1.linux-amd64.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.17.1.linux-amd64.tar.gz
ENV PATH $PATH:/usr/local/go/bin
ENV PATH $PATH:${HOME}/go/bin
RUN go version

WORKDIR /home/${HOME}
COPY . .

WORKDIR /home/${HOME}
RUN go install github.com/rubenv/sql-migrate/...

COPY startup.sh /startup.sh
RUN chmod 744 /startup.sh
CMD ["/startup.sh"]
