# Pull base image
FROM resin/rpi-raspbian:stretch
MAINTAINER cutech <cody@c-u-tech.com>

# Install dependencies
RUN mkdir /opt/jdk && apt-get update && apt-get upgrade -y && apt-get install screen sudo nano wget && wget -O /opt/jdk/jdk-8u151-linux-arm32-vfp-hflt.tar.gz --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie"  https://edelivery.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-arm32-vfp-hflt.tar.gz &&  tar -zvxf jdk-8u151-linux-arm32-vfp-hflt.tar.gz -C /opt/jdk && mkdir /nukkit && wget -O /nukkit/nukkit.jar http://ci.mengcraft.com:8080/job/nukkit/638/artifact/target/nukkit-1.0-SNAPSHOT.jar /nukkit/nukkit.jar
# Define working directory
WORKDIR /nukkit
