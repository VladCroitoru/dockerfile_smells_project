FROM ubuntu:16.04

ENV VERSION="1.69.1"

ENV INSTALL_PATH="/usr/local/bin/sentry-cli"
ENV DOWNLOAD_URL="https://github.com/getsentry/sentry-cli/releases/download/$VERSION/sentry-cli-Linux-x86_64"
RUN apt-get update && apt-get install -y wget
RUN wget -O "$INSTALL_PATH" "$DOWNLOAD_URL"
RUN chmod 0755 "$INSTALL_PATH"

ENTRYPOINT ["sentry-cli"]
CMD  ["--help"]
