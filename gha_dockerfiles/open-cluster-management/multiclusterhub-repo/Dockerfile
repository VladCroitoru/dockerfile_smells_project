# Copyright Contributors to the Open Cluster Management project

# Build the manager binary
FROM golang:1.17 as builder

WORKDIR /workspace

# Copy the Go Modules manifests
COPY go.mod go.mod
COPY go.sum go.sum

# cache deps before building and copying source so that we don't need to re-download as much
# and so that source changes don't invalidate our downloaded layer
RUN go mod download

# Copy the go source
COPY . .

# Build
RUN go build -o start-repo ./cmd/repo

FROM registry.access.redhat.com/ubi8/ubi-minimal:latest
RUN microdnf install tar
RUN microdnf update

LABEL org.label-schema.vendor="Red Hat" \
      org.label-schema.name="multiclusterhub-repo" \
      org.label-schema.description="Helm repo that serves charts for the Red Hat Advanced Cluster Management installer" \
      org.label-schema.license="Red Hat Advanced Cluster Management for Kubernetes EULA"

WORKDIR /app
COPY --from=builder /workspace/start-repo .
COPY multiclusterhub/charts/ multiclusterhub/charts/
EXPOSE 3000
ENTRYPOINT /app/start-repo