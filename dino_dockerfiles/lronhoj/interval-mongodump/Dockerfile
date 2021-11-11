FROM golang:1.9

# cause dependencies to be statically linked
ENV CGO_ENABLED=0

WORKDIR /go/src/app
COPY . .
RUN go build -o interval-mongodump main.go


FROM mongo:3.2
VOLUME /backup
COPY --from=0 /go/src/app/interval-mongodump /
ENTRYPOINT []
CMD ["/interval-mongodump"]
