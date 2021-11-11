FROM java:7-jre

MAINTAINER Jonathan Gimeno <jgimeno@gmail.com>

# Set last version
ENV NUTCH_VERSION 1.11

# Set java env Variable
ENV JAVA_HOME /usr

# Download nutch
RUN wget -q http://apache.rediris.es/nutch/$NUTCH_VERSION/apache-nutch-$NUTCH_VERSION-bin.zip

# Set nutch directory
ENV NUTCH_ROOT /nutch-$NUTCH_VERSION

# Unzip donwnloaded binaries
RUN unzip apache-nutch-$NUTCH_VERSION-bin.zip

RUN rm apache-nutch-$NUTCH_VERSION-bin.zip

RUN mv apache-nutch-$NUTCH_VERSION/ /nutch

# Data volume for nutch
VOLUME ["/data"]

# set workdir to nutch folder
WORKDIR /nutch

# Nutch server port.
EXPOSE 8899
