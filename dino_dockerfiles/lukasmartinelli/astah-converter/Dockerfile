FROM ubuntu:14.04
MAINTAINER Lukas Martinelli <me@lukasmartinelli.ch>

# install basic tools
ENV DEBIAN_FRONTEND noninteractive
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y byobu curl git htop man unzip vim wget && \
  rm -rf /var/lib/apt/lists/*

# install node
RUN curl --silent --location https://deb.nodesource.com/setup_0.12 | bash -
RUN apt-get install --yes nodejs

# install oracle jdk7
RUN \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java7-installer && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk7-installer

# install astah
RUN wget http://cdn.change-vision.com/files/astah-professional-6_9_0-b4c6e9.zip
RUN unzip astah-professional-6_9_0-b4c6e9.zip -d /opt && rm astah-professional-6_9_0-b4c6e9.zip
RUN chmod +x /opt/astah_professional/astah-command.sh

# install app
RUN mkdir -p /var/astah-converter/projects && \
    mkdir -p /var/astah-converter/exports && \
    mkdir -p /var/astah-converter/uploads && \
    mkdir -p /opt/astah-converter
COPY . /opt/astah-converter
WORKDIR /opt/astah-converter
RUN npm install

ENV ASTAH_DIR=/opt/astah_professional
ENV PROJECT_DIR=/var/astah-converter/projects
ENV EXPORT_DIR=/var/astah-converter/exports
ENV UPLOAD_DIR=/var/astah-converter/uploads
EXPOSE 3000
CMD ["nodejs", "server.js"]
