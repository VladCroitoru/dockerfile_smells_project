FROM debian:jessie

RUN apt-get update && apt-get install -y --no-install-recommends cron

VOLUME ["/etc/cron.d"]

CMD ["cron", "-f"]
