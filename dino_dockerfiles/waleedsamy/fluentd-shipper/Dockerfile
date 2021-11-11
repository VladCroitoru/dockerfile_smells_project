FROM fluent/fluentd
MAINTAINER Waleed Samy <waleedsamy634@gmail.com>

USER root
RUN mkdir -p /var/log/fluent/forward
RUN chown fluent:fluent /var/log/fluent/forward

USER fluent
WORKDIR /home/fluent
ENV PATH /home/fluent/.gem/ruby/2.3.0/bin:$PATH
COPY fluent.conf /fluentd/etc/

EXPOSE 24224

ENV FLUENTD_OUT_PORT 24224

CMD exec fluentd -c /fluentd/etc/$FLUENTD_CONF -p /fluentd/plugins $FLUENTD_OPT
