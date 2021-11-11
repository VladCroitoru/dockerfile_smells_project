FROM alpine:latest
MAINTAINER Sergey Ugdyzhekov, sergey@ugdyzhekov.org

RUN apk --no-cache add openssl jq bash curl
RUN wget https://github.com/barnybug/cli53/releases/download/0.8.7/cli53-linux-386 -O /usr/local/bin/cli53 && \
    chmod +x /usr/local/bin/cli53

RUN wget https://raw.githubusercontent.com/lukas2511/dehydrated/master/dehydrated -O /usr/local/bin/dehydrated && \
    chmod +x /usr/local/bin/dehydrated

RUN wget https://raw.githubusercontent.com/whereisaaron/dehydrated-route53-hook-script/master/hook.sh -O /usr/local/lib/route53_hook.sh && \
    chmod +x /usr/local/lib/route53_hook.sh

RUN echo -e 'CHALLENGETYPE="dns-01"\nHOOK=/usr/local/lib/route53_hook.sh\nHOOK_CHAIN="no"' > /etc/dehydrated.conf

WORKDIR /workbench

ENTRYPOINT ["/usr/local/bin/dehydrated", "--config", "/etc/dehydrated.conf", "-c", "--out", "."]
