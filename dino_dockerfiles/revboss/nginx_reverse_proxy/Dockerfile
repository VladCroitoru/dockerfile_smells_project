FROM nginx:stable

COPY nginx.conf /etc/nginx/nginx.conf
COPY startup.sh /usr/local/bin/startup.sh
RUN chmod 755 /usr/local/bin/startup.sh && \
  mkdir -p /etc/nginx/sites-available && \
  mkdir -p /etc/nginx/sites-enabled

ENTRYPOINT startup.sh 