FROM golang:1.9 as builder
WORKDIR /go/src/github.com/gugahoi/junit-report-converter
COPY . .
RUN CGO_ENABLED=0 go build -v -o /opt/junit-report-converter

FROM scratch
COPY --from=builder /opt/junit-report-converter /junit-report-converter
ENTRYPOINT [ "/junit-report-converter" ]