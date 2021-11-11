FROM rabbitmq:management
ENV AUTOCLUSTER_VERSION=0.10.0

RUN mkdir /var/lib/rabbitmq/plugins
ADD https://github.com/rabbitmq/rabbitmq-autocluster/releases/download/${AUTOCLUSTER_VERSION}/autocluster-${AUTOCLUSTER_VERSION}.ez /plugins/
ADD https://github.com/rabbitmq/rabbitmq-autocluster/releases/download/${AUTOCLUSTER_VERSION}/rabbitmq_aws-${AUTOCLUSTER_VERSION}.ez /plugins/
RUN chmod 644 /plugins/autocluster-${AUTOCLUSTER_VERSION}.ez /plugins/rabbitmq_aws-${AUTOCLUSTER_VERSION}.ez \
	&& rabbitmq-plugins enable autocluster --offline
