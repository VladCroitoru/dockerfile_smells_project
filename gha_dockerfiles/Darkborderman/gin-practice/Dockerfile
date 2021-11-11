FROM golang:1.16
WORKDIR /app/
COPY go.mod go.sum /app/
RUN go mod download && go install github.com/swaggo/swag/cmd/swag@v1.7.3
COPY . /app/
RUN /go/bin/swag init
RUN go build .
CMD ./practice
