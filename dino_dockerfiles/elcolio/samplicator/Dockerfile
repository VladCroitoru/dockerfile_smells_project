FROM ubuntu:latest
MAINTAINER Cole Brumley <cole.brumley@gmail.com>
ADD https://samplicator.googlecode.com/files/samplicator-1.3.7-beta6.tar.gz samplicator-1.3.7-beta6.tar.gz
RUN apt-get update && apt-get -y install tar build-essential
RUN tar xvf samplicator-1.3.7-beta6.tar.gz
WORKDIR samplicator-1.3.7-beta6
RUN ./configure
RUN make
RUN ln -s /samplicator-1.3.7-beta6/samplicate /usr/bin/samplicate
ENTRYPOINT ["samplicate"]
