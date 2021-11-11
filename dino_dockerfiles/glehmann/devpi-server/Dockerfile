FROM alpine
ARG version=2.2.0

RUN apk add --update py-pip \
  && pip install devpi==${version} pip-autoremove \
  && pip-autoremove -y pip-autoremove devpi-web \
  && rm -rf /var/cache/apk/* /root/.cache

VOLUME /data
EXPOSE 3141
ADD run.sh /
ENV DEVPI_SERVERDIR=/data \
    DEVPI_CLIENTDIR=/tmp/devpi-client
CMD ["/run.sh"]
