FROM golang:1.16-buster AS builder

ADD . /src

RUN cd /src \
  && go get -u -v golang.org/x/lint/golint \
  && go mod tidy \
  && go mod download \
  && golint . \
  && export CI=1 \
  && go test -covermode=count -coverprofile=coverage.out \
  && cat coverage.out | grep -v "http_whois.go" | grep -v "domain_whois.go" | grep -v "main.go" > coverage.txt \
  && TOTAL_COVERAGE_FOR_CI_F=$(go tool cover -func coverage.txt | grep total | grep -Eo '[0-9]+.[0-9]+') \
  && echo "TOTAL_COVERAGE_FOR_CI_F: $TOTAL_COVERAGE_FOR_CI_F" \
  && CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o whois-json


FROM scratch

COPY --from=builder /src/whois-json /usr/bin/whois-json

ENTRYPOINT ["/usr/bin/whois-json"]
