FROM governmentpaas/curl-ssl
RUN apk add --update bash && rm -rf /var/cache/apk/*
RUN curl -o /usr/local/bin/fly "https://ci.concourse.ci/api/v1/cli?arch=amd64&platform=linux"
RUN chmod +x /usr/local/bin/fly
