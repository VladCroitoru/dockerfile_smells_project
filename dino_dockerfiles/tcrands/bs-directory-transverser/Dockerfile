FROM golang:1.7

RUN mkdir /bs-directory-transverser
RUN mkdir /source

WORKDIR /bs-directory-transverser

ADD . /bs-directory-transverser

RUN go build

RUN cp ./bs-directory-transverser /usr/bin

WORKDIR /source

CMD ["bs-directory-transverser"]
