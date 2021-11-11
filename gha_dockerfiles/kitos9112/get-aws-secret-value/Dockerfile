FROM golang:1.17.3-alpine AS build
RUN apk add --no-cache make jq
WORKDIR /go/src/github.com/kitos9112/get-aws-secret-value.git/
COPY . .
ENV CGO_ENABLED=0
RUN make binaries/linux_x86_64/get-aws-secret-value && mv binaries/linux_x86_64/get-aws-secret-value /app

FROM alpine:3.14
RUN apk add --no-cache ca-certificates
COPY --from=build /app /bin/get-aws-secret-value
CMD [ "get-aws-secret-value" ]
