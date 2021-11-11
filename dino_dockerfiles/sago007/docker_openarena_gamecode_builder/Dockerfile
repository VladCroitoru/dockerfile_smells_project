FROM debian:8
MAINTAINER poul@poulsander.com
RUN apt-get update && \
    apt-get install -y build-essential bison zip git
COPY gamecode_build_script.bash /
RUN mkdir /data && \
    mkdir /working && \
    mkdir /extra2pk3 && \
    chmod 777 /working && \
    chmod 777 /gamecode_build_script.bash

COPY extra2pk3 /extra2pk3/

#Result will be placed in this folder
VOLUME ["/data"]

#Ensure that the user is allowed to place files in /data
USER nobody

CMD /gamecode_build_script.bash
