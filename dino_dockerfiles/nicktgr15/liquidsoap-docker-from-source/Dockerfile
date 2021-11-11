FROM savonet/liquidsoap-deps

USER opam

WORKDIR /tmp

USER root

RUN apt-get update -y
RUN apt-get install wget -y 
RUN apt-get install vim -y

USER opam

RUN wget https://github.com/savonet/liquidsoap/releases/download/1.3.3/liquidsoap-1.3.3-full.tar.gz 
RUN tar -zxf liquidsoap-1.3.3-full.tar.gz

WORKDIR /tmp/liquidsoap-1.3.3-full

RUN cp PACKAGES.minimal PACKAGES

RUN eval $(opam config env) && ./configure && make clean && make

USER root

RUN make install

USER opam

RUN openssl req -x509 -newkey rsa:4096 -sha256 -nodes -keyout /tmp/server.key -out /tmp/server.crt -subj "/CN=localhost" -days 3650

COPY my.liq /my.liq

ENTRYPOINT liquidsoap --verbose /my.liq
