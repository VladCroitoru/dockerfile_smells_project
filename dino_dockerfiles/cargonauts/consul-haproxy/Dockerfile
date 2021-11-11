FROM debian:wheezy

ADD backports.list /etc/apt/sources.list.d/backports.list
RUN apt-get update && apt-get install -y haproxy -t wheezy-backports

ADD https://github.com/hashicorp/consul-template/releases/download/v0.8.0/consul-template_0.8.0_linux_amd64.tar.gz  /consul-template.tar.gz
RUN tar xzvf /consul-template.tar.gz --strip-components=1 && rm /consul-template.tar.gz

ADD haproxy.ctmpl /haproxy.ctmpl

EXPOSE 80

ENTRYPOINT ["/consul-template"]
CMD ["-consul", "consul:8500", "-template", "/haproxy.ctmpl:/etc/haproxy/haproxy.cfg:service haproxy reload"]
