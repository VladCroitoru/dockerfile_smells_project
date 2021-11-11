FROM golang:1.6.0-alpine

MAINTAINER Carlos León, mail@carlosleon.info

RUN apk add --update git
RUN git clone https://github.com/mongrelion/gapp.git /opt/gapp
RUN cd /opt/gapp && go build -o /bin/gapp .
ENTRYPOINT ["/bin/gapp"]

EXPOSE 8080
