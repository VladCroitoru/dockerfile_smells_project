FROM madpeter/phpapachepreload:latest

MAINTAINER Madpeter

COPY --chown=www-data:www-data . /srv/website
COPY .docker/vhost.conf /etc/apache2/sites-available/000-default.conf

WORKDIR /srv/website

RUN chmod +x .docker/CronEntrypoint.sh \
    && chmod +x .docker/CronEntrypointWithBot.sh \
    && chmod +x .docker/CronEntrypointAndExporter.sh \
    && chmod +x .docker/CronEntrypointWithBotAndExporter.sh \
    && chmod +x .docker/Exporter.sh \
    && apt-get update