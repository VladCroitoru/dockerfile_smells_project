FROM nginx

MAINTAINER Greg Keys <gkeys@mumbacloud.com>

ENV VAULT_VERSION 0.5.2
ENV VAULT_TMP /tmp/vault.zip
ENV VAULT_HOME /usr/local/bin
ENV PATH $PATH:${VAULT_HOME}

EXPOSE 80 443

COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
        curl \
        jq \
        git \
        cron \
        python-pip \
        openssl \
        coreutils \
        wget \
        unzip \
        ca-certificates \
    && wget --quiet --output-document=${VAULT_TMP} https://releases.hashicorp.com/vault/${VAULT_VERSION}/vault_${VAULT_VERSION}_linux_amd64.zip \
    && unzip ${VAULT_TMP} -d ${VAULT_HOME} \
    && rm -f ${VAULT_TMP} \
    && git clone --depth 1 https://github.com/letsencrypt/letsencrypt /opt/letsencrypt \
    && /opt/letsencrypt/letsencrypt-auto -h > /dev/null \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && crontab -l 2>/dev/null; echo "30 2 * * 1 /opt/letsencrypt/letsencrypt-auto renew --webroot -w /usr/share/nginx/html/ && nginx -s reload" | crontab - \
    && rm -rf /tmp/* /usr/share/man /var/cache/apk/* /root/.npm /root/.node-gyp /root/.gnupg \
           /usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html /root/.npmrc /var/lib/{apt,dpkg,cache,log}/

CMD ["nginx", "-g", "daemon off;"]