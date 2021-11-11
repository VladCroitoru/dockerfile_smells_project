FROM golang:alpine AS build

ADD vendor /go/src/github.com/tjamet/google-jwt/vendor
ADD *.html *.go /go/src/github.com/tjamet/google-jwt/
RUN go generate github.com/tjamet/google-jwt/
RUN go build -o /usr/local/bin/google-jwt github.com/tjamet/google-jwt/

FROM alpine
RUN apk add --no-cache ca-certificates
COPY --from=build /usr/local/bin/google-jwt /google-jwt
ENTRYPOINT ["/google-jwt"]