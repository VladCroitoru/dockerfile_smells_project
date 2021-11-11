FROM alpine:latest
MAINTAINER Sergey Ugdyzhekov, sergey@ugdyzhekov.org

RUN apk --no-cache add openssl jq bash curl

RUN wget https://raw.githubusercontent.com/lukas2511/dehydrated/master/dehydrated -O /usr/local/bin/dehydrated && \
    chmod +x /usr/local/bin/dehydrated

RUN wget https://raw.githubusercontent.com/sugdyzhekov/dehydrated-selectel-dns-hook-script/master/hook.sh -O /usr/local/lib/selectel_dns_hook.sh && \
    chmod +x /usr/local/lib/selectel_dns_hook.sh

RUN echo -e 'CHALLENGETYPE="dns-01"\nHOOK=/usr/local/lib/selectel_dns_hook.sh\nHOOK_CHAIN="no"' > /etc/dehydrated.conf

WORKDIR /workbench

ENTRYPOINT ["/usr/local/bin/dehydrated", "--config", "/etc/dehydrated.conf", "-c", "--out", "."]
