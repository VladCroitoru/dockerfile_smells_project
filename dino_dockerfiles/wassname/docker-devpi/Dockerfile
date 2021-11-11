FROM python:3.4-slim
MAINTAINER wassname@wassname.org

RUN pip --no-cache-dir install --upgrade \
  "devpi-client>=2.3" "requests>=2.9.0" \
  "devpi-server==2.5.3"

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

EXPOSE 3141
VOLUME /data
WORKDIR /data
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["devpi"]
