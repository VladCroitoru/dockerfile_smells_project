FROM       golang:1.15.6
WORKDIR    /go/src/github.com/proofpoint/certificate-init-container
ADD        . .
RUN        go install -mod vendor -a && \
           go test -mod vendor ./...

FROM gcr.io/distroless/base-debian10:nonroot

COPY --from=0 /go/bin/certificate-init-container /
ENTRYPOINT ["/certificate-init-container"]
