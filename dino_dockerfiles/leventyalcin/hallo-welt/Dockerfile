# build instructions:
# img_name=$(grep '^LABEL ' ./Dockerfile | sed -e 's/.*Name="\([^"]\+\).*/\1/')
# tag_version=$(grep '^LABEL ' ./Dockerfile | sed -e 's/.*Version="\([^"]\+\).*/\1/')
# docker build --no-cache=true --rm --tag $img_name:$tag_version .
# docker rmi $img_name:stable 2>/dev/null
# docker tag $img_name:$tag_version $img_name:stable
#
#
# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang:1.7.1

LABEL Name="hallo-welt" Version="0.0.1" \
      Description="https://www.youtube.com/watch?v=57D-IpL46IM"

MAINTAINER leventyalcin

RUN go get github.com/leventyalcin/hallo-welt \
    && go install github.com/leventyalcin/hallo-welt

ENTRYPOINT [ "/go/bin/hallo-welt" ]

EXPOSE 8080
