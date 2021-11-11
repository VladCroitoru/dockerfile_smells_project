FROM rabbitmq:3-management
LABEL maintainer="Health Catalyst"
LABEL version="1.0"

RUN apt-get update \
    && apt-get install openssl \
	&& apt-get install tofrodos \
    && ln -s /usr/bin/fromdos /usr/bin/dos2unix	

# update erlang
RUN apt-get install -y wget \
    && echo 'deb http://packages.erlang-solutions.com/debian stretch contrib' | tee /etc/apt/sources.list.d/erlang.list \
    && wget https://packages.erlang-solutions.com/debian/erlang_solutions.asc \
    && apt-key add erlang_solutions.asc \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
		erlang-asn1 \
		erlang-crypto \
		erlang-eldap \
		erlang-inets \
		erlang-mnesia \
		erlang-nox \
		erlang-os-mon \
		erlang-public-key \
		erlang-ssl \
		erlang-xmerl

# COPY openssl.cnf /opt/healthcatalyst/testca

COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config
COPY rabbitmq_nossl.config /etc/rabbitmq/rabbitmq_nossl.config

ADD my-docker-entrypoint.sh ./my-docker-entrypoint.sh
ADD setupusers.sh ./setupusers.sh

RUN dos2unix ./my-docker-entrypoint.sh \
	&& chmod +x ./my-docker-entrypoint.sh \
	&& dos2unix ./setupusers.sh \
	&& chmod +x ./setupusers.sh 


COPY plugins/* /usr/lib/rabbitmq/lib/rabbitmq_server-3.6.12/plugins/

ENTRYPOINT [ "./my-docker-entrypoint.sh" ]