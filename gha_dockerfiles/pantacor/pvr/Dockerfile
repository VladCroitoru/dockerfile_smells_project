FROM golang:alpine as src

ENV GO111MODULES=on

WORKDIR /app/
COPY . .

ARG DOCKERTAG=latest
RUN apk update; apk add git
RUN version=`git describe --tags` && sed -i "s/NA/$version/" version.go
RUN sed -i "s/defaultDistributionTag = \"develop\"/defaultDistributionTag = \"${DOCKERTAG}\"/" ./libpvr/configurationlib.go
RUN go get

# build riscv64 linux static
FROM src as linux_riscv64

RUN apk update; apk add git
RUN CGO_ENABLED=0 GOOS=linux GOARCH=riscv64 go build -o /go/bin/linux_arm64/pvr -v .


# build amd64 linux static
FROM src as linux_amd64

RUN apk update; apk add git
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /go/bin/linux_amd64/pvr -v .

# build armv6 linux static
FROM src as linux_armv6

RUN apk update; apk add git
RUN CGO_ENABLED=0 GOOS=linux GOARCH=arm GOARM=5 go build -o /go/bin/linux_armv6/pvr -v .

# build armv6 linux static
FROM src as linux_arm64

RUN apk update; apk add git
RUN CGO_ENABLED=0 GOOS=linux GOARCH=arm64 GOARM=5 go build -o /go/bin/linux_arm64/pvr -v .


# build windows i386 static
FROM src as windows_386

RUN apk update; apk add git
RUN CGO_ENABLED=0 GOOS=windows GOARCH=386 go build -o /go/bin/windows_386/pvr.exe -v .

# build windows amd64 static
FROM src as windows_amd64

RUN apk update; apk add git
RUN CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build -o /go/bin/windows_amd64/pvr.exe -v .

# build darwin amd64 static
FROM src as darwin_amd64

RUN apk update; apk add git
RUN CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build -o /go/bin/darwin_amd64/pvr -v .


FROM alpine

RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*

WORKDIR /work
COPY --from=linux_amd64 /go/bin /pkg/bin
COPY --from=linux_armv6 /go/bin /pkg/bin
COPY --from=windows_386 /go/bin /pkg/bin
COPY --from=windows_amd64 /go/bin /pkg/bin
COPY --from=darwin_amd64 /go/bin /pkg/bin

ENV USER root

ENTRYPOINT [ "/bin/tar", "-C", "/pkg/", "-c", "." ]

