
FROM fluent/fluentd
MAINTAINER Peter Mechlenborg <peter@humio.com>
LABEL Description="Docker 2 Humio custom fluentd shipper"

#WORKDIR /home/fluent
#ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH

#USER root


COPY fluent.conf /fluentd/etc/

RUN apk add --update --virtual .build-deps \
        sudo build-base ruby-dev \
 && sudo gem install \
        fluent-plugin-elasticsearch \
 && sudo gem sources --clear-all \
 && apk del .build-deps \
 && rm -rf /var/cache/apk/* \
           /home/fluent/.gem/ruby/2.3.0/cache/*.gem

#EXPOSE 24224

#USER fluent
#CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT
