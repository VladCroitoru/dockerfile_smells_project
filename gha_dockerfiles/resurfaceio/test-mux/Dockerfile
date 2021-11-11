FROM golang:1.16
RUN apt -y update && apt -y install python3 python3-pip

WORKDIR /app

COPY /src .
COPY run-test.sh .

RUN go mod download
RUN pip3 install git+https://github.com/resurfaceio/logger-test-engine@master
RUN go build .

CMD ["./test-mux"]