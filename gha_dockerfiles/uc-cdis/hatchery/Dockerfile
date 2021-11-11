FROM quay.io/cdis/golang:1.17-bullseye as build-deps

ENV CGO_ENABLED=0
ENV GOOS=linux
ENV GOARCH=amd64

WORKDIR $GOPATH/src/github.com/uc-cdis/hatchery/

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

RUN GITCOMMIT=$(git rev-parse HEAD) \
    GITVERSION=$(git describe --always --tags) \
    && go build \
    -ldflags="-X 'github.com/uc-cdis/hatchery/hatchery/version.GitCommit=${GITCOMMIT}' -X 'github.com/uc-cdis/hatchery/hatchery/version.GitVersion=${GITVERSION}'" \
    -o /hatchery

FROM scratch
COPY --from=build-deps /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=build-deps /hatchery /hatchery
CMD ["/hatchery"]
