FROM node:16-alpine as build-front

WORKDIR /usr/src/qa/front
COPY . .
WORKDIR /usr/src/qa/front/examples/qa/assets/flagship-qa-front

RUN npm install
RUN npm run build-bundle

FROM golang:1-alpine as build-env

WORKDIR /go/src/github.com/flagship-io/flagship-go-sdk

# COPY the source code as the last step
COPY . .

WORKDIR /go/src/github.com/flagship-io/flagship-go-sdk/examples

# Get dependancies - will also be cached if we won't change mod/sum
RUN go mod download

# Build the binary
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -o /go/bin/example qa/*.go

# Run the binary
FROM alpine

EXPOSE 8080

WORKDIR /go/bin

COPY --from=build-env /go/bin/example example
COPY --from=build-env /go/src/github.com/flagship-io/flagship-go-sdk/examples/qa/assets/index.html qa/assets/index.html
COPY --from=build-front /usr/src/qa/front/examples/qa/assets/flagship-qa-front qa/assets/flagship-qa-front

CMD ["./example"]