FROM happyholic1203/devbox
MAINTAINER Yu-Cheng (Henry) Huang

RUN echo "deb http://www.rabbitmq.com/debian/ testing main" >> /etc/apt/sources.list && \
    curl http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | sudo apt-key add - && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq mysql-server \
        python-mysqldb rabbitmq-server && \
    rabbitmq-plugins enable rabbitmq_management && \
    pip install sqlalchemy pika

# Default entry point for happyholic1203/devbox
CMD ["/root/init"]
