FROM digitalr00ts/os:alpine

# Maintainer
LABEL maintainer="mgolly@users.noreply.github.com"


# Install SaltStack
ARG SALT_VERSION=2017.7.5
RUN apk add --no-cache linux-pam py-pyldap netcat-openbsd curl py-pip py-openssl salt-api salt-cloud salt-master salt-minion salt-ssh salt-syndic && \
    rm -rf -- /var/cache/apk/* /var/lib/apk/* /etc/apk/cache/* /root/.cache && \
    pip --no-cache-dir install CherryPy GitPython croniter salt==$SALT_VERSION && \
    mkdir -p \
      /etc/salt/master.d \
      /etc/salt/pki/master/minions \
      /etc/salt/pki/api \
      /srv/salt \
      /var/cache/salt \
      /var/log/salt && \
    chmod -R 700 /etc/salt/pki/master


# Install Molten
ARG MOLTEN_VERSION=0.3.1
ARG MOLTEN_MD5=04483620978a3167827bdd1424e34505
RUN wget https://github.com/martinhoefling/molten/releases/download/v${MOLTEN_VERSION}/molten-${MOLTEN_VERSION}.tar.gz && \
    echo "${MOLTEN_MD5}  molten-${MOLTEN_VERSION}.tar.gz" | md5sum -c && \
    mkdir -p /opt/molten && \
    tar -xf molten-${MOLTEN_VERSION}.tar.gz -C /opt/molten --strip-components=1 && \
    rm molten-${MOLTEN_VERSION}.tar.gz


# Default master config
COPY config/* /etc/salt/master.d/

# Copy healthcheck and run scripts
COPY scripts/* /usr/local/bin/


# Volumes
VOLUME ["/etc/salt/master.d", "/etc/salt/pki", "/srv/salt", "/var/cache/salt", "/var/log/salt"]

# Expose ports for salt & salt-api/molten
EXPOSE 4505 4506 443

# Healthcheck
HEALTHCHECK --interval=1m --timeout=3s --start-period=20s --retries=3 \
  CMD nc -zw 1 localhost 4505 && nc -zw 1 localhost 4506 && /usr/local/bin/test-api.py || exit 1

# Launch supervisor
CMD ["/usr/local/bin/run.sh"]
