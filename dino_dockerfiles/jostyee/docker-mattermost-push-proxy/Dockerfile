FROM frolvlad/alpine-glibc:alpine-3.7
LABEL maintainer="jostyee <hi@josta.me>"

ENV MATTERMOST_VERSION=4.10.1

RUN apk add --no-cache ca-certificates curl \
	&& curl -sSL https://github.com/mattermost/mattermost-push-proxy/releases/download/v${MATTERMOST_VERSION}/mattermost-push-proxy-${MATTERMOST_VERSION}.tar.gz | tar -xz \
	&& mv /mattermost-push-proxy/bin/mattermost-push-proxy /push-proxy \
	&& chmod +x /push-proxy \
	&& rm -rf /mattermost-push-proxy \
	&& apk del curl

EXPOSE 8066
ENTRYPOINT ["/push-proxy"]
