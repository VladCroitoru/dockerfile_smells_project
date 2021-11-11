FROM rabbitmq:3.6-management
ADD https://bintray.com/rabbitmq/community-plugins/download_file?file_path=rabbitmq_delayed_message_exchange-0.0.1.ez /usr/lib/rabbitmq/lib/rabbitmq_server-${RABBITMQ_VERSION}/plugins/rabbitmq_delayed_message_exchange-0.0.1.ez
RUN chown -R rabbitmq:rabbitmq /usr/lib/rabbitmq/lib/rabbitmq_server-${RABBITMQ_VERSION}/plugins/ \
        && rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange

