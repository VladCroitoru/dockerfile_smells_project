FROM quay.io/bitriseio/bitrise-base
RUN apt-get install ca-certificates -y \
    && update-ca-certificates --fresh
RUN go get github.com/codegangsta/gin \
    && go get github.com/kisielk/errcheck \
    && go get -u golang.org/x/lint/golint
ADD . /bitrise/src
RUN go mod download
