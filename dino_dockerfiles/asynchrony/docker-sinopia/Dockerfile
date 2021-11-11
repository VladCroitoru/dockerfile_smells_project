FROM node:4-slim

WORKDIR /root

RUN npm install -g verdaccio@2.1.7 verdaccio-ldap@1.1.0 \
 && mkdir /root/sinopia \
 && apt-get update \
 && apt-get install -y curl --no-install-recommends \
 && rm -rf /var/lib/apt/lists/* \
 && curl -sSL https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 -o /usr/bin/confd \
 && echo "dd4479abccb24564827dcf14fcb73ccc5bba8aeb /usr/bin/confd" | sha1sum -c - \
 && chmod +x /usr/bin/confd \
 && apt-get purge -y --auto-remove curl

COPY confd /etc/confd
COPY start.sh /start.sh

EXPOSE 4873

CMD ["/start.sh"]
