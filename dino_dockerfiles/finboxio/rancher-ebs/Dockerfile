FROM alpine:edge

RUN apk add --no-cache curl bash xfsprogs groff less python py-pip && \
    curl -L -o /usr/bin/jq https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 && \
    chmod +x /usr/bin/jq && \
    pip install awscli && \
    apk del --no-cache py-pip

COPY ebs-scripts/* /usr/sbin/
RUN chmod +x /usr/sbin/ebs-*

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
