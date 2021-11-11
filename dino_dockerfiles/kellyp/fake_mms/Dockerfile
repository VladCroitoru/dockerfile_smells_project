# build fake mms
FROM golang:alpine as golang
WORKDIR /go/src/app
COPY . .

RUN CGO_ENABLED=0 go build -ldflags '-extldflags "-static"' -o fake_mms

# install fake mms
FROM scratch

COPY --from=golang /go/src/app/fake_mms /fake_mms

EXPOSE 8080/tcp

# run fake mms
ENTRYPOINT [ "/fake_mms" ]
