FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    openjdk-8-jdk \
    curl \
    unzip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install activator

ENV ACTIVATOR_VERSION 1.3.10

RUN curl -O http://downloads.typesafe.com/typesafe-activator/$ACTIVATOR_VERSION/typesafe-activator-${ACTIVATOR_VERSION}-minimal.zip \
    && unzip typesafe-activator-${ACTIVATOR_VERSION}-minimal.zip -d / \
    && rm typesafe-activator-${ACTIVATOR_VERSION}-minimal.zip \
    && chmod a+x /activator-${ACTIVATOR_VERSION}-minimal/bin/activator

ENV PATH $PATH:/activator-${ACTIVATOR_VERSION}-minimal/bin

# Get and compile veritask

RUN cd /home && git clone https://github.com/BonarBeavis/Veritask.git
WORKDIR /home/Veritask
RUN activator clean stage

EXPOSE 9000

CMD target/universal/stage/bin/veritask -Dplay.crypto.secret=abcdefghijk
