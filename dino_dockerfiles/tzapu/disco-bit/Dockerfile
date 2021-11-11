#FROM golang:1.9

# Set go bin which doesn't appear to be set already.
#ENV GOBIN /go/bin

# build directories
#RUN mkdir /app
#RUN mkdir /go/src/app
#ADD . /go/src/app
#WORKDIR /go/src/app

#RUN git rev-parse --short HEAD

# Go dep!
#RUN go get -u github.com/golang/dep/...
#RUN dep ensure

# Build my app
#RUN go build -o /app/main .
#ENTRYPOINT ["/app/main"]


FROM golang:1.8

WORKDIR /go/src/app
COPY . .

RUN go-wrapper download   # "go get -d -v ./..."
RUN go-wrapper install    # "go install -v ./..."

ENTRYPOINT ["go-wrapper", "run"] # ["app"]