FROM golang:alpine AS builder

# Create an unprivileged user
RUN adduser \    
    --disabled-password \    
    --gecos "" \    
    --home "/nonexistent" \    
    --shell "/sbin/nologin" \    
    --no-create-home \    
    --uid 10001 \    
    appuser

# Get CA certs required for HTTPS. Git is required for dependencies.
RUN apk update  && apk upgrade && apk add --no-cache git

# Set working directory /src (default dir is /go)
WORKDIR /src
COPY . .

# access to private repos (e.g. Bitbucket)
ARG NETRC
RUN echo $NETRC > ~/.netrc
RUN go env -w GOPRIVATE=github.com/el-zacharoo/*

# Build as static-linked binary (no external dependencies).
RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -o /app

# Build minimal image (800mb -> 15Mb)
FROM scratch

COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app /app

EXPOSE 8080
# Perform any further action as an unprivileged user
USER appuser:appuser
ENTRYPOINT ["/app"]