ARG BASE_IMG=golang:1.16-buster

FROM ${BASE_IMG} AS builder

RUN apt update

RUN mkdir -p /usr/src/app/

ADD . /usr/src/app

WORKDIR /usr/src/app/

RUN make web-build

RUN make migrate-build

FROM builder AS dev

RUN apt-get update -qq \
	&& apt install -yq --no-install-recommends nano vim

# Install air for local development
RUN curl -sSfL https://raw.githubusercontent.com/cosmtrek/air/master/install.sh | sh -s -- -b $(go env GOPATH)/bin

#CMD ["./scripts/run-web.sh"]

FROM ${BASE_IMG} AS prod

RUN apt-get update -qq \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \
	jq \
	&& apt-get clean \
	&& rm -rf /var/cache/apt/archives/* \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& truncate -s 0 /var/log/*log

WORKDIR /app

COPY --from=builder /usr/src/app/ /app

RUN useradd app-user -m \
	&& chown -R app-user:app-user /app

RUN mkdir -p -m 775 tmp \
	&& chown -R app-user:app-user tmp

USER app-user

#CMD ["./scripts/run-web.sh"]
