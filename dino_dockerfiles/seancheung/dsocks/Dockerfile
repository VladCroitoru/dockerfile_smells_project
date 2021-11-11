FROM python:2-alpine
MAINTAINER Sean Dheung <theoxuanx@gmail.com>

RUN pip install shadowsocks

VOLUME ["/etc/shadowsocks"]

EXPOSE 1080

ENTRYPOINT ["/usr/local/bin/ssserver"]

CMD ["-c", "/etc/shadowsocks/config.json", "start"]