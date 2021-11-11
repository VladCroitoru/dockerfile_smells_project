FROM golang:1.13
ARG TIMEZONE="America/Sao_Paulo"
RUN set -x \
    && apt-get update \
    && apt-get upgrade -y \
    && echo "=> Needed packages:" \
    && apt-get install -y --no-install-recommends apt-utils curl ca-certificates tar openssl xz-utils \
    && echo "=> Configuring and installing timezone (${TIMEZONE}):" \
    && echo ${TIMEZONE} > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove apt-utils

WORKDIR /go/src/app
RUN go get -u github.com/golang/dep/cmd/dep
COPY . .
RUN dep ensure && go build && go install
CMD ["app"]