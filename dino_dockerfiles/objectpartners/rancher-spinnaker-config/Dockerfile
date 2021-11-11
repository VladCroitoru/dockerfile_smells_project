FROM rancher/confd-base:0.11.0-dev-rancher

VOLUME /opt/spinnaker/config
VOLUME /root/.aws

ENTRYPOINT ["/confd"]
CMD ["--backend", "rancher", "--prefix", "/2015-07-25"]

ADD ./conf.d /etc/confd/conf.d
ADD ./templates /etc/confd/templates
