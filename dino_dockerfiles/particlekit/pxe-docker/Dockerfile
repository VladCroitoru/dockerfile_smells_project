FROM httpd

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    tftpd-hpa --no-install-recommends

ENV TFTPOPTIONS="--secure --port-range 3000:4000"

EXPOSE 80 69

VOLUME ["/usr/local/apache2/htdocs","/srv/tftp"]

ADD init.sh /

CMD ["/init.sh"]
