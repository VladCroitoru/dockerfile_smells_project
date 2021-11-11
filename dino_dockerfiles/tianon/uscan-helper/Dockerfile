FROM golang:1.15-alpine3.13

RUN apk add --no-cache git

WORKDIR /usr/src/uscan-helper
COPY . .
RUN go install -v -mod=vendor

EXPOSE 8181
CMD ["uscan-helper"]
