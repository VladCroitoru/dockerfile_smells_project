FROM golang

MAINTAINER Nane Kratzke

# Copy sources
ADD src /pingpong/src

# Install dependencies
ENV GOPATH /pingpong/
RUN go get github.com/gorilla/mux
RUN go install pingpong

EXPOSE 8080

ENTRYPOINT ["/pingpong/bin/pingpong"]
CMD ["-port 8080 -asPong"]
