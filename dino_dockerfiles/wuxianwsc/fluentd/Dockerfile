FROM debian:8
RUN apt-get update && apt-get install -y curl sudo && \
curl -L https://toolbelt.treasuredata.com/sh/install-debian-jessie-td-agent2.sh | sh
WORKDIR /
COPY start.sh /start.sh
RUN touch /tmp/fluentd.pos && chown td-agent.td-agent /tmp/fluentd.pos && chmod +x /start.sh
CMD ["td-agent"]
