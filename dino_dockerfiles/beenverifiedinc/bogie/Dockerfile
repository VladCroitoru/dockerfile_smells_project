FROM golang:1.13-alpine AS build
RUN apk --no-cache update && \
    apk --no-cache add make ca-certificates git && \
    rm -rf /var/cache/apk/*
WORKDIR /go/src/github.com/BeenVerifiedInc/bogie
COPY go.mod /go/src/github.com/BeenVerifiedInc/bogie
COPY go.sum /go/src/github.com/BeenVerifiedInc/bogie
RUN go mod download
COPY . ./
RUN	CGO_ENABLED=0 GOOS=linux go build -installsuffix cgo -ldflags \
    "-X github.com/BeenVerifiedInc/bogie/version.Version=`git describe --tags` -X github.com/BeenVerifiedInc/bogie/version.Commit=`git log -n 1 --pretty=format:"%h"`" \
    -o bin/bogie

FROM scratch AS bogie
LABEL mainainer="Scott Wagner <swagner@beenverified.com>"
COPY --from=build /etc/ssl/certs/ /etc/ssl/certs/
COPY --from=build /go/src/github.com/BeenVerifiedInc/bogie/bin/bogie /usr/local/bin/bogie
ENTRYPOINT ["/usr/local/bin/bogie"]
CMD ["--help"]
