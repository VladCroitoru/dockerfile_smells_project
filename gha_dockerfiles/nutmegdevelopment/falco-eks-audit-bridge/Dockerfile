FROM golang:1.17-alpine AS builder

WORKDIR /app

COPY . .

ENV USER=nutmeg
ENV UID=10001
RUN adduser \
		--disabled-password \
		--gecos "" \
		--home "/nonexistent" \
		--shell "/sbin/nologin" \
		--no-create-home \
		--uid "${UID}" \
		"${USER}" && \
	apk update && apk add --no-cache git ca-certificates && \
	go mod download && \
	go mod verify && \
    CGO_ENABLED=0 GOARCH=amd64 GOOS=linux go build -ldflags="-w -s" -o falco-eks-audit-bridge -v

FROM scratch

COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/falco-eks-audit-bridge /app/falco-eks-audit-bridge
USER nutmeg:nutmeg

ENTRYPOINT ["/app/falco-eks-audit-bridge"]

