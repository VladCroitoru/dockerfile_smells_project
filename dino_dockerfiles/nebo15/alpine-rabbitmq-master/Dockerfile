FROM nebo15/alpine-rabbitmq-node:3.6.6
MAINTAINER Nebo#15 <support@nebo15.com>

# Enable sentitel plugins
RUN rabbitmq-plugins enable --offline \
        rabbitmq_management \
        rabbitmq_management_visualiser \
        rabbitmq_shovel_management \
        rabbitmq_tracing && \
  rabbitmq-plugins list

        # rabbitmq_federation_management \

EXPOSE 15671 15672
