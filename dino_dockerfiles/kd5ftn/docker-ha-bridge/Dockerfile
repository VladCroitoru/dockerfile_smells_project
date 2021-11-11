#Resin.io produces base ARM images for raspberry pi. This one adds QEMU support in order to support cross-building (for DockerHub to build ARM projects)
FROM codingwell/rpi-raspbian-qemu:latest

RUN [ "cross-build-start" ]

MAINTAINER Nick McCarthy

#Volumes will be added via docker run command
#VOLUME ["/config"]
RUN apt-get update && \
    apt-get upgrade && \
    apt-get install -y curl wget oracle-java8-jdk 

    
RUN mkdir -p /root/habridge/ && \
    cd /root/habridge && \
    VERSION="$(curl -sX GET https://api.github.com/repos/bwssytems/ha-bridge/releases/latest | grep 'tag_name' | cut -d\" -f4 | cut -b 1 --complement)" && \
    wget https://github.com/bwssytems/ha-bridge/releases/download/v"$VERSION"/ha-bridge-"$VERSION".jar && \   
    mv ha-bridge-"$VERSION".jar ha-bridge.jar

CMD [ "java","-jar","-Dserver.port=80","/root/habridge/ha-bridge.jar" ]

RUN [ "cross-build-end" ]
