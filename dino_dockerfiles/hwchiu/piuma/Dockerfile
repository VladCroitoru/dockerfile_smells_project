FROM golang:1.8-onbuild

RUN go get github.com/lotrekagency/piuma
RUN apt-get -y update &&\
    apt-get install -y pngquant jpegoptim

ENTRYPOINT ["piuma"]
