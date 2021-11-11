FROM debian:jessie

MAINTAINER Frederic GRACIA <gracia.frederic@gmail.com>

# Installing packages
RUN apt-get update && \
    apt-get install -y \
    python-pip \
    python-dev \
    libffi-dev \
    libssl-dev \
    libsqlite3-dev \
    python-cheetah \
    git-core \
    wget \
    unrar-free

# Cleaning APT cache
RUN apt-get clean

# Compiling and installing Python2.7.13
WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
RUN tar xzf Python-2.7.13.tgz
WORKDIR /usr/src/Python-2.7.13
RUN ./configure
RUN make install

WORKDIR /root

# Creating data directory (for future app config files)
RUN mkdir /data

# App installation
ADD tmp /opt/SickRage

# Copying startup script
COPY ./startup.sh /startup.sh
RUN chmod +x /startup.sh

# Exposing app port
EXPOSE 8081

# Running app
CMD ["/startup.sh"]
