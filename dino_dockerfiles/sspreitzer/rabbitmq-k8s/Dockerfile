FROM rabbitmq:management

ADD assets/rabbitmq.conf /etc/rabbitmq/rabbitmq.conf

RUN rabbitmq-plugins enable --offline rabbitmq_peer_discovery_k8s
