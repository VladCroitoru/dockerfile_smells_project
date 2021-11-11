FROM golang:1.10.2 AS builder
COPY Makefile /go/src/github.com/mpppk/gored/Makefile
WORKDIR /go/src/github.com/mpppk/gored
RUN make setup
COPY . /go/src/github.com/mpppk/gored
RUN make install

FROM circleci/golang:1.10.2
COPY --from=builder /go/bin/* /go/bin/
RUN git config --global user.email "gored-bot@dammy.com"
RUN git config --global user.name  "gored-bot"
USER root
RUN mkdir /init
RUN chown circleci /init
USER circleci
CMD cd /init && gored init