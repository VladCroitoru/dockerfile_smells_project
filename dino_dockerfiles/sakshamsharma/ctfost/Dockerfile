FROM golang:1.6

RUN apt-get update
RUN bash -c "yes | apt-get install cgroup-bin sudo"
COPY cgconfig.conf /etc/cgconfig.conf

RUN mkdir -p /go/src/app
WORKDIR /go/src/app

# this will ideally be built by the ONBUILD below ;)
CMD ["go-wrapper", "run"]

COPY . /go/src/app
RUN go-wrapper download
RUN go-wrapper install

EXPOSE 4002
