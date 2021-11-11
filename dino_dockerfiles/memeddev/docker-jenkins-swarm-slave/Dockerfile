FROM openjdk:jre
MAINTAINER memed <gabriel.couto@memed.com.br>

# Installing packages
RUN apt-get update && apt-get upgrade -y
RUN export DEBIAN_FRONTEND=noninteractive && apt-get install -y --force-yes git

ADD assets/ /assets
WORKDIR /assets

# Cleaning
RUN apt-get clean && apt-get autoremove -y