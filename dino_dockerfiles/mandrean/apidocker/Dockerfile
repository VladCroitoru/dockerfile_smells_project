FROM alpine:latest

MAINTAINER Sebastian Mandrean <sebastian.mandrean@gmail.com>

# Install nodejs & apidoc
RUN apk add --no-cache nodejs && npm install apidoc -g

# Clean up
RUN rm -rf ~/.npm && npm cache clear

ENV APIDOCKER_INPUT=/
ENV APIDOCKER_OUTPUT=docs/
WORKDIR /src

ENTRYPOINT apidoc -i $APIDOCKER_INPUT -o $APIDOCKER_OUTPUT
