FROM golang:1.16 as builder

WORKDIR /workspace
COPY go.mod go.mod
COPY go.sum go.sum
RUN go mod download

COPY main.go main.go
COPY api/ api/
COPY controllers/ controllers/
COPY errors/ errors/
COPY gateways/ gateways/
COPY services/ services/
COPY utils/ utils/
COPY wire/ wire/

#RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -o manager main.go
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -tags osusergo,netgo -a -o manager main.go


#FROM gcr.io/distroless/static:nonroot
FROM alpine:3.13.6
WORKDIR /
RUN apk add -u git
COPY --from=builder /workspace/manager .
USER 65532:65532

ENTRYPOINT ["/manager"]
