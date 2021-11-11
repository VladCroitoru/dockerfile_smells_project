FROM huggla/varnish-alpine

ENV JAIL="unix,user=varnish" \
    STORAGE="deprecated_persistent,/varnishcache/cache,100M"

COPY ./bin/pre-entry.sh /usr/local/bin/pre-entry.sh

RUN mkdir /varnishcache \
 && chown varnish:varnish /varnishcache \
 && chmod ugo+x /usr/local/bin/pre-entry.sh

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["pre-entry.sh && entry.sh"]
