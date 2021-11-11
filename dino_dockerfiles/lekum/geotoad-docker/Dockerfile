FROM ubuntu:17.10
LABEL maintainer="Alejandro Guirao <lekumberri@gmail.com>"
ENV REFRESHED_AT 2018-02-11

RUN apt-get -qqy update
RUN apt-get -qqy install ruby git

RUN mkdir -p /opt/geotoad
RUN mkdir -p /opt/gpx
RUN git clone https://github.com/steve8x8/geotoad.git /opt/geotoad

WORKDIR /opt/geotoad
RUN echo `cat VERSION`+`date +%Y%m%d`-`git log | head -n1 | cut -c8-14` > GEOTOAD_VERSION
RUN sed -i s/%VERSION%/`cat GEOTOAD_VERSION`/g lib/version.rb
RUN sed -i s/%VERSION%/`cat GEOTOAD_VERSION`/g README.txt
RUN sed -i s/%VERSION%/`cat GEOTOAD_VERSION`/g FAQ.txt

ENTRYPOINT [ "/opt/geotoad/geotoad.rb" ]
CMD []
