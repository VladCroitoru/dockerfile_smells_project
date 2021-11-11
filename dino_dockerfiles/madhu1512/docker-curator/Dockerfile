FROM alpine:3.6

RUN apk --update add python py-setuptools py-pip && \
    pip install --upgrade pip && \
    pip install elasticsearch-curator==5.1.1 && \
    apk del py-pip && \
    rm -rf /var/cache/apk/*


COPY config/curator.yml /root/.curator/curator.yml
ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
