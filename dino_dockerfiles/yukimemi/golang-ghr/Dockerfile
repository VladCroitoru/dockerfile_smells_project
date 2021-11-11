# Golang
#
# VERSION       0.0.1

FROM golang
MAINTAINER yukimemi <yukimemi@gmail.com>

RUN apt update \
      && apt install -y --no-install-recommends \
      zip \
      && rm -rf /var/lib/apt/lists/*

RUN go get -u github.com/tcnksm/ghr \
      && go get -u github.com/motemen/gobump/cmd/gobump

RUN curl -o /usr/local/bin/jq -L https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 \
      && chmod +x /usr/local/bin/jq \
      && curl -sL "https://github.com/Masterminds/glide/releases/download/v0.12.3/glide-v0.12.3-linux-amd64.tar.gz" | \
      tar xz \
        -C /usr/local/bin/ \
        --strip=1 \
        --wildcards --wildcards-match-slash '*/glide' \
        --no-same-owner \
        --no-same-permissions

COPY ./compile.sh /usr/bin/compile
COPY ./release.sh /usr/bin/release

