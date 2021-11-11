FROM golang:alpine AS build
WORKDIR /go/src/app
COPY hello.go .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" hello.go

FROM scratch
COPY --from=build /go/src/app .
CMD ["/hello"] 
