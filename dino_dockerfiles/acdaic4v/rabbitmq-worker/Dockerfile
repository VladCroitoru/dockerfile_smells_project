# Dockerfile acdaic4v/rabbitmq-worker
FROM acdaic4v/ubuntu-perl-rabbitmq:v20170330
MAINTAINER acdaic4v <acdaic4v@sloervi.de>

LABEL Description="Create Docker Image that acts as a RabbitMQ Worker" Vendor="acdaic4v" Version="1"

# Get my scripts
RUN cd /usr/local/bin && git clone https://github.com/acdaic4v/rabbitmq-worker.git rabbitmq-worker
# Install rabbitmqctl to add users, change password : No: Do it on the server
# RUN apt-get update && apt-get install -y rabbitmqctl 
  
# Create User and group
RUN groupadd -r rabbit && useradd -r -g rabbit rabbit
RUN chown -R rabbit /usr/local/bin/rabbitmq-worker
RUN chmod u+x /usr/local/bin/rabbitmq-worker/rabbitmq-worker.pl
USER rabbit

# YAML File with Configuration
VOLUME /usr/local/etc/rabbitmq-worker/
# Your Script to run
VOLUME /usr/local/bin/myworker/
# Worker included in this Image / Container
ENTRYPOINT /usr/local/bin/rabbitmq-worker/rabbitmq-worker.pl
