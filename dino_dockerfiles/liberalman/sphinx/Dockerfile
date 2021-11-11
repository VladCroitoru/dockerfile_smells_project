FROM alpine:latest
MAINTAINER liberalman liberalman@github.com

# reference https://github.com/romeOz/docker-sphinxsearch

# install sphinx
#RUN apk --update --no-cache add runit sphinx
RUN apk --update add sphinx

ENV SPHINX_CONF=/etc/sphinx/sphinx.conf

COPY sphinx.conf ${SPHINX_CONF}
COPY entrypoint.sh /sbin/entrypoint.sh

RUN chmod 755 /sbin/entrypoint.sh \
    && ln -sf /dev/stdout /var/lib/sphinx/log/searchd.log \
    && ln -sf /dev/stdout /var/lib/sphinx/log/query.log

EXPOSE 9312 9306
ENTRYPOINT ["/sbin/entrypoint.sh"]


