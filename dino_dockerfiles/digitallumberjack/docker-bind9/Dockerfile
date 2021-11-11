FROM debian:jessie

ENV BIND9_IP ''
ENV BIND9_ROOTDOMAIN ''
ENV BIND9_KEYNAME ''
ENV BIND9_KEY ''
ENV BIND9_FORWARDERS '8.8.8.8;8.8.4.4;'
ENV BIND9_IPV4ONLY ''
ENV BIND9_QUERY_CACHE_ACCEPT '127.0.0.1;'
ENV BIND9_RECURSION_ACCEPT '127.0.0.1;'
ENV BIND9_STATIC_ENTRIES ''
ENV LC_ALL en_US.UTF-8

RUN apt-get update -qq

RUN echo "locales locales/locales_to_be_generated multiselect en_US.UTF-8 UTF-8" | debconf-set-selections &&\
    echo "locales locales/default_environment_locale select en_US.UTF-8" | debconf-set-selections
RUN apt-get install locales bind9 curl -qq && apt-get clean

COPY start.sh /usr/local/bin/

RUN mkdir -p /var/run/named /etc/bind/zones

CMD ["/usr/local/bin/start.sh"]
