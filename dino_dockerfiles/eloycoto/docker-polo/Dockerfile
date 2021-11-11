FROM golang
MAINTAINER Eloy Coto <eloy.coto@gmail.com>

RUN go get github.com/agonzalezro/polo
RUN mkdir /source/
RUN mkdir /web/

ADD config.json .
ADD source /source/

WORKDIR /

VOLUME ["/web/"]

CMD ["polo", "/source/", "/web/"]
