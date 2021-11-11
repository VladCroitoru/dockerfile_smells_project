FROM alpine

LABEL maintainer="Henrik Jonsson <me@hkjn.me>"

RUN apk add --no-cache bash ruby git

ENV GOPATH /go
ENV BINPATH $GOPATH/bin/hkjn.me/rr
WORKDIR $BINPATH

ADD git-wtf.rb ./
COPY ["rr", "./"]
ENV PATH $PATH:$BINPATH

ENTRYPOINT ["rr", "-alsologtostderr"]
CMD [""]
