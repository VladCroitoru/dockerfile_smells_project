FROM nginx:stable-alpine

LABEL maintainer="Erin Schnabel <schnabel@us.ibm.com> (@ebullientworks)"

# support running as arbitrary user which belogs to the root group
RUN touch /var/run/nginx.pid \
 && chown -R nginx:root /var/run/nginx.pid \
 && chown -R nginx:root /var/cache/nginx \
 && chmod g+rwx /var/cache/nginx /var/run/nginx.pid /var/log/nginx

COPY ./nginx.conf   /etc/nginx/nginx.conf
COPY ./startup.sh   /opt/startup.sh

ENV VERSION=3.4.3

RUN mkdir -p /opt/www \
  && wget https://github.com/swagger-api/swagger-ui/archive/v${VERSION}.tar.gz -q \
  && tar xzvf v${VERSION}.tar.gz --strip-components=2 -C /opt/www swagger-ui-${VERSION}/dist \
  && rm v${VERSION}.tar.gz

COPY ./lib/crypto-js/* /opt/www/lib/crypto-js/
COPY ./index.html /opt/www/index.html

COPY ./gameontext.json /opt/www/
COPY ./gameontext.yaml /opt/www/

USER nginx
EXPOSE 8080

ENTRYPOINT ["/opt/startup.sh"]

HEALTHCHECK \
  --timeout=10s \
  --start-period=40s \
  CMD wget -q -O /dev/null http://localhost:8080/health
