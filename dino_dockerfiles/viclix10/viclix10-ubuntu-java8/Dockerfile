#
# Ubuntu & Oracle Java 8 Dockerfile
#
#

# Pull base image.
FROM ubuntu

# Install Java.
RUN \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  apt-get install -y software-properties-common && \
  add-apt-repository ppa:webupd8team/java -y && \
  apt-get update && \
  apt-get install -y oracle-java8-installer && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Define working directory.
WORKDIR /data
ADD . /data

# Define default command.
CMD ["bash"]

CMD ["ls -al /data/"]
CMD ["ls -al /data/temp/"]
CMD ["cat /data/temp"]
