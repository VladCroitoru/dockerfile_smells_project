FROM alpine:latest

WORKDIR /src

ARG APPLICATION="myapp"
ARG BUILD_RFC3339="1970-01-01T00:00:00Z"
ARG REVISION="local"
ARG DESCRIPTION="no description"
ARG PACKAGE="user/repo"
ARG VERSION="dirty"

LABEL org.opencontainers.image.ref.name="${PACKAGE}" \
	org.opencontainers.image.created=$BUILD_RFC3339 \
	org.opencontainers.image.authors="Justin J. Novack <jnovack@gmail.com>" \
	org.opencontainers.image.documentation="https://github.com/${PACKAGE}/README.md" \
	org.opencontainers.image.description="${DESCRIPTION}" \
	org.opencontainers.image.licenses="MIT" \
	org.opencontainers.image.source="https://github.com/${PACKAGE}" \
	org.opencontainers.image.revision=$REVISION \
	org.opencontainers.image.version=$VERSION \
	org.opencontainers.image.url="https://hub.docker.com/r/${PACKAGE}/"

RUN \
	apk add --no-cache git openssh

COPY checkout.sh /

ENV USER=appuser
ENV UID=10001
RUN adduser \
	--disabled-password \
	--gecos "" \
	--home "/home/${USER}" \
	--shell "/sbin/nologin" \
	--uid "${UID}" \
	"${USER}"
USER appuser:appuser

ENTRYPOINT [ "/checkout.sh" ]
