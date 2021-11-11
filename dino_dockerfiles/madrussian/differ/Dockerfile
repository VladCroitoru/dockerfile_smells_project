FROM ubuntu:14.04
MAINTAINER Nodar Nutsubidze <nodar.nutsubidze@gmail.com>
ENV HOSTNAME localhost

# Install packages
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -qy \
  git \
  python-pip

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -qy \
  python-dev

# Download git repo
RUN git clone https://github.com/MadRussian/differ.git /opt/differ

# Move to the directory so we install the libraries in correct folder
RUN cd /opt/differ && make

WORKDIR /opt/differ
CMD ["make", "test"]
