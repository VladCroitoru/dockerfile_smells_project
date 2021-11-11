FROM larrytalley/activemq-docker-image
MAINTAINER Larry TALLEY <larry.talley@gmail.com>

ENV ACTIVEMQ_NAME messagebus1 \
    ACTIVEMQ_REMOVE_DEFAULT_ACCOUNT true \
    ACTIVEMQ_ADMIN_LOGIN admin \
    ACTIVEMQ_ADMIN_PASSWORD admin \
    ACTIVEMQ_WRITE_LOGIN producer_login \
    ACTIVEMQ_WRITE_PASSWORD producer_password \
    ACTIVEMQ_READ_LOGIN consumer_login \
    ACTIVEMQ_READ_PASSWORD consumer_password \
    ACTIVEMQ_JMX_LOGIN jmx_login \
    ACTIVEMQ_JMX_PASSWORD jmx_password \
    ACTIVEMQ_STATIC_TOPICS log;auth;akfish \
    ACTIVEMQ_STATIC_QUEUES queue1;queue2;queue3 \
    ACTIVEMQ_MIN_MEMORY 1024 \
    ACTIVEMQ_MAX_MEMORY 4096 \
    ACTIVEMQ_ENABLED_SCHEDULER true

CMD ["/bin/sh", "-c", "$ACTIVEMQ_HOME/bin/activemq console"]
