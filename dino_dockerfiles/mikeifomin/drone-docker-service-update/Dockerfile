FROM golang:1.9 as compiler

COPY . /go/src/github.com/mikeifomin/drone-docker-service-update/
WORKDIR /go/src/github.com/mikeifomin/drone-docker-service-update/

RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0         go build -ldflags "-X main.build=${DRONE_BUILD_NUMBER}" -a -tags netgo -o /release/linux/amd64/drone-docker github.com/mikeifomin/drone-docker-service-update/cmd/drone-docker

FROM docker:17.10.0-ce-dind
COPY --from=compiler /release/linux/amd64/drone-docker /bin/
ENTRYPOINT ["/usr/local/bin/dockerd-entrypoint.sh", "/bin/drone-docker"]
