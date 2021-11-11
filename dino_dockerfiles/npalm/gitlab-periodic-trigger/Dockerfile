FROM alpine:3.5
MAINTAINER Niek Palm <dev.npalm@gmail.com>

# Install curl
RUN apk add --update --no-cache curl

# Copy trigger script
COPY trigger-gitlab.sh /usr/local/bin
RUN chmod +x /usr/local/bin/trigger-gitlab.sh

ONBUILD COPY gitlabcrontab /etc/crontabs/root
ONBUILD RUN chmod 0600 /etc/crontabs/root

CMD ["crond", "-f", "-d", "8"]
