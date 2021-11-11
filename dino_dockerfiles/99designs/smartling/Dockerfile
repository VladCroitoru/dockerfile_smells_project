FROM golang:1.15

COPY . /smartling
RUN cd /smartling && go mod download && go install ./...
RUN mkdir /work
WORKDIR /work

ENTRYPOINT ["smartling"]
