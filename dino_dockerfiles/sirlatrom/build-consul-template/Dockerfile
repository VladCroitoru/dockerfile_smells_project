FROM golang:1.6beta2

ENV VERSION=0.12.2

RUN git clone https://github.com/hashicorp/consul-template.git /go/src/github.com/hashicorp/consul-template

WORKDIR /go/src/github.com/hashicorp/consul-template

RUN git reset --hard v$VERSION

# Fails without being piped to true
RUN make updatedeps || /bin/true

CMD make dev
