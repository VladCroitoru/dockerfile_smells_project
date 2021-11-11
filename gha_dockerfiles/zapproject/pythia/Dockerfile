FROM golang:stretch

WORKDIR /go/delivery

RUN apt -y update
RUN apt -y install ocl-icd-opencl-dev

COPY . .

RUN echo {} > config.json

RUN chmod +x serve.sh
RUN chmod +x mine.sh
RUN chmod +x release_build.sh

RUN unset GOPATH
RUN ./release_build.sh
