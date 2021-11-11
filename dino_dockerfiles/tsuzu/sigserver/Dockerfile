# Copyright (c) 2018 tsuzu
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

FROM golang:1.10

RUN mkdir /sigserver
COPY ./config.template.toml /sigserver/config.toml
RUN go get github.com/cs3238-tsuzu/sigserver

ENTRYPOINT [ "sigserver", "--config", "/sigserver/config.toml" ]
