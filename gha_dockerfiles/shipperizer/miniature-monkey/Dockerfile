FROM golang:1.16 AS builder

ENV GO111MODULE=on
ENV CGO_ENABLED=0
ENV GOOS=linux

RUN apt-get update
RUN apt-get install -y awscli

RUN mkdir -p -m 0600 /root/.ssh
RUN ssh-keyscan github.com >> ~/.ssh/known_hosts
RUN git config --global url.ssh://git@github.com/.insteadOf "https://github.com/"
COPY id_rsa /root/.ssh/id_rsa

WORKDIR /var/app

COPY . .
