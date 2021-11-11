# Build stage: create the binary
FROM golang:1.8 AS build-environment

# Install glide
RUN go get github.com/Masterminds/glide

# Install tools
RUN apt-get update \
    && apt-get install -y \
        python-pip \
        python-virtualenv \
    && apt-get clean

ENV INODEBEAT_PATH "$GOPATH/src/github.com/codingame/inodebeat"

WORKDIR $INODEBEAT_PATH

COPY glide.yaml glide.lock $INODEBEAT_PATH/

# Install dependencies
RUN glide install

COPY . $INODEBEAT_PATH

# Create inodebeat binary
RUN make update \
    && make \
    && mkdir -p /usr/share/inodebeat \
    && cp inodebeat \
        inodebeat.yml \
        inodebeat.full.yml \
        inodebeat.template-es2x.json \
        inodebeat.template-es6x.json \
        inodebeat.template.json \
        /usr/share/inodebeat


# Final stage: create the actual image
FROM debian:jessie

ENV INODEBEAT_HOME=/usr/share/inodebeat

WORKDIR $INODEBEAT_HOME

ENV PATH $INODEBEAT_HOME:$PATH

COPY --from=build-environment $INODEBEAT_HOME $INODEBEAT_HOME

CMD [ "inodebeat", "-c", "$INODEBEAT_HOME/inodebeat.yml", "-e" ]
