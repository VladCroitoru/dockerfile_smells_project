FROM nouchka/symfony:7.0

ARG FUNC_NAME=faas-symfony
ARG FUNC_PACKAGE=jq

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -yq install curl ${FUNC_PACKAGE} \
	&& echo "Pulling watchdog binary from Github." \
	&& curl -sSL https://github.com/openfaas/faas/releases/download/0.7.6/fwatchdog > /usr/bin/fwatchdog \
	&& chmod +x /usr/bin/fwatchdog \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

##CUSTOM
RUN mkdir -p /var/www/ && cd /var/www/ && composer create-project symfony/skeleton my-command && mkdir -p my-command/src/Command/ && chown -R www-data: /var/www/
USER www-data
COPY TestCommand.php my-command/src/Command/TestCommand.php
##CUSTOM

COPY func.sh /usr/bin/${FUNC_NAME}
ENV fprocess="/usr/bin/${FUNC_NAME}"
ENV write_debug="true"

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1
CMD [ "fwatchdog" ]
