FROM golang:latest

MAINTAINER Dao Anh Dung <dung13890@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV GO111MODULE=on
ENV GOFLAGS=-mod=vendor

RUN apt-get update
RUN apt-get install -y graphviz protobuf-compiler
