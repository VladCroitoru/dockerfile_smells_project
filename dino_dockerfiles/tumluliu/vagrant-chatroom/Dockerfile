# 
# Web chat demo in Scala
#
# https://github.com/playframework/play-java-chatroom-example
#

# Pull the base image
FROM hseeberger/scala-sbt:8u141-jdk_2.12.3_1.0.1

# Install git
RUN \
  apt-get update && \
  apt-get install git

# Clone chatroom repo
RUN \
  git clone https://github.com/playframework/play-java-chatroom-example.git /chatroom

# Define working directory
WORKDIR /chatroom

# Compile chatroom with sbt
RUN \
  sbt clean test compile
