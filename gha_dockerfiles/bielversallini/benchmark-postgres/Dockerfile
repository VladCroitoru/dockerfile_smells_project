FROM registry.ci.openshift.org/open-cluster-management/builder:go1.16-linux AS builder

WORKDIR /go/src/github.com/jlpadilla/benchmark-postgres
COPY . .
RUN CGO_ENABLED=0 go build -trimpath -o main main.go

FROM registry.access.redhat.com/ubi8/ubi-minimal:8.4

COPY --from=builder /go/src/github.com/jlpadilla/benchmark-postgres/main /bin/main
COPY --from=builder /go/src/github.com/jlpadilla/benchmark-postgres/data ./data

ENV USER_UID=1001 \
    GOGC=25

USER ${USER_UID}
ENTRYPOINT ["/bin/main"]