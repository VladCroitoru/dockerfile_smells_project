FROM rabbitmq

RUN echo '[ \
  {rabbit, [{auth_backends, [rabbit_auth_backend_http]}]}, \
  {rabbitmq_amqp1_0, [{default_user, none},{default_vhost, <<"/">>},{protocol_strict_mode, false}]}, \
  {rabbitmq_auth_backend_http, \
   [{user_path,     "https://meshblu-amqp-auth.octoblu.com/user"}, \
    {vhost_path,    "https://meshblu-amqp-auth.octoblu.com/vhost"}, \
    {resource_path, "https://meshblu-amqp-auth.octoblu.com/resource"}]} \
].' > /etc/rabbitmq/rabbitmq.config

ADD http://www.rabbitmq.com/community-plugins/v3.6.x/rabbitmq_auth_backend_http-3.6.x-3dfe5950.ez /plugins/
RUN chmod 777 /plugins/*

RUN rabbitmq-plugins enable --offline rabbitmq_amqp1_0
RUN rabbitmq-plugins enable --offline rabbitmq_auth_backend_http
RUN rabbitmq-plugins enable --offline rabbitmq_auth_mechanism_ssl
