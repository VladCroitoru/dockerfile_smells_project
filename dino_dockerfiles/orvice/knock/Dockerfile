FROM golang:1.9 as builder

## Create a directory and Add Code
RUN mkdir -p /go/src/github.com/orvice/knock
WORKDIR /go/src/github.com/orvice/knock
ADD .  /go/src/github.com/orvice/knock

# Download and install any required third party dependencies into the container.
RUN go-wrapper download
RUN CGO_ENABLED=0 go build


FROM orvice/go-runtime

COPY --from=builder /go/src/github.com/orvice/knock/knock .


ENTRYPOINT [ "./knock" ]