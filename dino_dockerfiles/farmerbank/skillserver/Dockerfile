FROM golang:1.8-alpine

WORKDIR /go/src/app
COPY . .
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh
    
RUN go-wrapper download   # "go get -d -v ./..."
RUN go-wrapper install    # "go install -v ./..."
EXPOSE 3000
CMD ["go-wrapper", "run"] # ["app"]
