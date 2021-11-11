# Build container
FROM golang:1.11-alpine as BUILD

ENV CGO_ENABLED=0
ARG SOURCE_COMMIT=""
ARG SOURCE_BRANCH="develop"

WORKDIR /go/src/app
COPY . .

RUN apk add git --no-cache
RUN go get -d -v ./...
RUN go install -ldflags="-d -s -w -X main.SourceBranch=$SOURCE_BRANCH -X main.GolangVersion=$GOLANG_VERSION -X main.SourceCommit=$SOURCE_COMMIT" -v ./...

# Release container
FROM scratch as RELEASE

ENV GIN_MODE=release
ENV PORT=8080

COPY --from=BUILD /go/bin/* /usr/local/bin/
COPY ./static /static

EXPOSE 80 443 8080
ENTRYPOINT ["app"]
