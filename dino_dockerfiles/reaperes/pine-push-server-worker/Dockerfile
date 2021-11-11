FROM dockerfile/java:oracle-java8
MAINTAINER Namhoon (emerald105@hanmail.net)

# Install maven
RUN \
  export DEBIAN_FRONTEND=noninteractive && \
  apt-get update && \
  apt-get install -y maven

WORKDIR /root

# Run application
ADD ./start.sh /start.sh
RUN chmod +x /start.sh
