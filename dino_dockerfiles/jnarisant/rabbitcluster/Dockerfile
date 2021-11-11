FROM rabbitmq:management

ADD plugins/autocluster-0.7.0.ez \
/usr/lib/rabbitmq/lib/rabbitmq_server-$RABBITMQ_VERSION/plugins/

ADD plugins/autocluster_aws-0.0.1.ez \
/usr/lib/rabbitmq/lib/rabbitmq_server-$RABBITMQ_VERSION/plugins/

ADD plugins/rabbitmq_aws-0.7.0.ez \
/usr/lib/rabbitmq/lib/rabbitmq_server-$RABBITMQ_VERSION/plugins/

RUN rabbitmq-plugins enable --offline autocluster

# this is where its super custom
COPY pre-entrypoint.sh /
RUN chmod 550 /pre-entrypoint.sh

ENTRYPOINT ["/pre-entrypoint.sh"]
CMD ["rabbitmq-server"]