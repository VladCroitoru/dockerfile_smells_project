FROM ubuntu:16.04

ENV BIND9_IP ''
ENV BIND9_ROOTDOMAIN ''
ENV BIND9_KEYNAME ''
ENV BIND9_KEY ''
ENV BIND9_FORWARDERS '8.8.8.8;8.8.4.4;'
ENV BIND9_IPV4ONLY ''
ENV LC_ALL en_US.UTF-8

COPY start.sh /usr/local/bin/

RUN apt-get update -qq && \
  echo "locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8" | debconf-set-selections &&\
  echo "locales locales/default_environment_locale select en_US.UTF-8" | debconf-set-selections && \
  apt-get install locales bind9 curl -y -qq && \
  apt-get clean && \
  mkdir -p /var/run/named /etc/bind/zones && \
  chmod 775 /var/run/named && \
  chown root:bind /var/run/named 2>&1 && \
  chmod 775 -Rfc /etc/bind 2>&1 && \
  chown root:bind -Rfc /etc/bind 2>&1 && \
  chmod 775 /usr/local/bin/start.sh 2>&1 && \
  chown root:bind /usr/local/bin/start.sh 2>&1

USER bind

CMD ["/usr/local/bin/start.sh"]
