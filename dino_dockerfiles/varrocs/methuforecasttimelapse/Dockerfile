FROM golang
ADD . /go/src/github.com/varrocs/methuforecasttimelapse
RUN go install github.com/varrocs/methuforecasttimelapse

WORKDIR /go/src/github.com/varrocs/methuforecasttimelapse
ENTRYPOINT /go/bin/methuforecasttimelapse

EXPOSE 8080
