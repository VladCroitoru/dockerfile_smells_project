FROM debian:jessie
MAINTAINER Guilherme Barile "gui@bravado.com.br"


# Update the package repository
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get upgrade -y; \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends locales slapd ldap-utils && \
  apt-get clean

# Configure timezone and locale
RUN echo "America/Sao_Paulo" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata

VOLUME [ "/var/lib/ldap" ]

EXPOSE 389

# Set the locale
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

ENV OPENLDAP_DATABASE example.com
# If empty, OPENLDAP_SUFFIX is automatically derived from OPENLDAP_DATABASE
ENV OPENLDAP_SUFFIX ""
# If empty, OPENLDAP_ROOT_PASSWORD is automatically generated on first run
ENV OPENLDAP_ROOT_PASSWORD ""

ADD ./etc /etc

RUN chmod +x /etc/entrypoint.sh

ENTRYPOINT ["/etc/entrypoint.sh" ]
