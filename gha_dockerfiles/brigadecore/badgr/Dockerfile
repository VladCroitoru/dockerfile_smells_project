FROM --platform=$BUILDPLATFORM brigadecore/go-tools:v0.5.0 as builder

ARG VERSION
ARG COMMIT
ARG TARGETOS
ARG TARGETARCH
ENV CGO_ENABLED=0

WORKDIR /
COPY . /
COPY go.mod go.mod
COPY go.sum go.sum

RUN GOOS=$TARGETOS GOARCH=$TARGETARCH go build \
  -o bin/badgr \
  -ldflags "-w -X github.com/brigadecore/brigade-foundations/version.version=$VERSION -X github.com/brigadecore/brigade-foundations/version.commit=$COMMIT" \
  .

FROM scratch
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=builder /bin/ /badgr/bin/
ENTRYPOINT ["/badgr/bin/badgr"]
