FROM openjdk:alpine
LABEL maintainer="Dean Smith <dean@zelotus.com>"
ENV path /Techtonicus

ADD https://github.com/tectonicus/tectonicus/releases/download/v2.25/Tectonicus-2.25.zip Tectonicus-2.25.zip

RUN mkdir ${path}
RUN (cd ${path}; unzip ../Tectonicus-2.25.zip)
ADD simpleConfig.xml ${path}/simpleConfig.xml
ADD run.sh	     ${path}/run.sh

VOLUME ["/world"]
VOLUME ["/map"]

ENTRYPOINT /bin/sh ${path}/run.sh






