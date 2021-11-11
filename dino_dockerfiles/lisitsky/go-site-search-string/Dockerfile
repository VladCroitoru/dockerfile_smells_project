# build stage
#FROM golang:1.8 AS build-env
#ADD . /src
#RUN cd /src && go get -t -v github.com/lisitsky/go-site-search-string && go build -o goapp
#
## final stage
#FROM alpine
#WORKDIR /app
#COPY --from=build-env /src/goapp /app/
#ENTRYPOINT /goapp
#

###
# Basic image builder
FROM golang:onbuild AS builder
#EXPOSE 8080

#FROM golang:1.8
#
#WORKDIR /app
#ADD . /app
#
#RUN cd /app \
#	&& go get -t -v github.com/lisitsky/go-site-search-string \
#	&& go build -o goapp
#
##ENTRYPOINT ./goapp
#
#
## final stage
#FROM alpine
#WORKDIR /app
#COPY --from=0 /src/goapp /app/
#ENTRYPOINT ./goapp
#
#


#FROM builder

####
## Basic image builder
#FROM golang:1.8-onbuild  AS builder
#
##WORKDIR /Users/el/go/src/github.com/lisitsky/go-site-search-string
#
##RUN go version
##RUN go get -u -v -t github.com/lisitsky/go-site-search-string
#
##COPY main*.go /
#
##RUN go build -v -o go-site-search-string .
##RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo  github.com/lisitsky/go-site-search-string
#
##RUN ls; pwd
##ADD ./go-site-search-string /go-site-search-string
##CMD ["/go-site-search-string"]
#
#EXPOSE 8080
#
#
##
#####
###
#FROM alpine
##
#WORKDIR /
##
#COPY --from=builder /go/bin/app .
##
#EXPOSE 8080
##
##CMD ["/go/app"]
#CMD ["/app"]



#FROM golang:1.8
#
#RUN set -x && \
#	go get -u -v -t github.com/lisitsky/go-site-search-string && \
#	HTTP_TIMEOUT=1 go test -v -cover -race	&& \
#	go build github.com/lisitsky/go-site-search-string
#
#ADD ./go-site-search-string /go-site-search-string
#
#CMD ["/go-site-search-string"]
