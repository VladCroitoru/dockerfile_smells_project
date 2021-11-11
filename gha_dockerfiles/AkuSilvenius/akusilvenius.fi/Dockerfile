ARG BUILDER_IMAGE=golang:alpine

# STEP 0 build frontend
FROM node:16-alpine3.11 as build-node
RUN apk --no-cache --virtual build-dependencies add \
    python \
    make \
    g++

WORKDIR /workdir
COPY client/ .
RUN npm install
RUN npm run build

# STEP 1 build executable binary
FROM ${BUILDER_IMAGE} AS builder

# Install git + SSL ca certificates.
# Git is required for fetching the dependencies.
# Ca-certificates is required to call HTTPS endpoints.
RUN apk update && apk add --no-cache git ca-certificates tzdata && update-ca-certificates

# Create appuser
ENV USER=appuser
ENV UID=10001

# See https://stackoverflow.com/a/55757473/12429735
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"

WORKDIR $GOPATH/src/main/

RUN export GIN_MODE=release
ADD go.mod go.sum ./
RUN go mod download
ADD . .

# Build the binary
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build \
    -ldflags='-w -s -extldflags "-static"' -a \
    -o /go/bin/main .

############################
# STEP 2 build a small image
############################
FROM scratch

# Import from builder.
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group

# Copy our static executable + frontend build
COPY --from=builder /go/bin/main ./
COPY --from=build-node /workdir/build ./client/build

# Use an unprivileged user.
USER appuser:appuser

# Run the microservice-demo binary.
EXPOSE 5000
ENTRYPOINT [ "./main" ]