FROM debian:jessie
MAINTAINER David Parrish <david@dparrish.com>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y libwww-perl liberror-perl libnet-netmask-perl libnet-ssleay-perl

# Rollout Configuration
VOLUME /config/fragments
VOLUME /config/files

ADD rolloutd /usr/local/sbin/rolloutd
ADD rollout /config/rollout
ADD RolloutConfigValidator.pm /config/
ADD rollout.cfg /config/rollout.cfg
ADD steps /config/steps
ADD fragments /config/fragments

EXPOSE 8001
CMD ["/usr/local/sbin/rolloutd", "--base", "/config", "--allow", "0.0.0.0/0", "--listen", "0.0.0.0:8001", "--user", "nobody", "--group", "nobody", "--logfile", "/var/log/rolloutd.log"]
