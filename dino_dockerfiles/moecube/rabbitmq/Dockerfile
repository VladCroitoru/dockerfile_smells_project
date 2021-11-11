FROM rabbitmq:management
RUN apt update
RUN apt install -y curl bsdtar
RUN curl --retry 5 --location https://github.com/gmr/pgsql-listen-exchange/releases/download/0.3.0-v3.5.x/pgsql-listen-exchange-0.3.0-v3.5.x.zip | bsdtar -C plugins -xf -
RUN rabbitmq-plugins enable --offline rabbitmq_web_stomp pgsql_listen_exchange
