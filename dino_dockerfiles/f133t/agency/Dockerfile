
FROM f133t/fleet-base:latest

COPY ./ /opt/agency

WORKDIR /opt/agency

RUN \
  sudo chown -R ubuntu:ubuntu /opt/agency

USER ubuntu

RUN bundle install

ENTRYPOINT [".docker/docker-entrypoint.sh"]
