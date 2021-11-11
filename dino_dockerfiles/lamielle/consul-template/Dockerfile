FROM progrium/busybox
MAINTAINER Alan LaMielle <alan.lamielle+github@gmail.com>

ADD https://github.com/hashicorp/consul-template/releases/download/v0.6.5/consul-template_0.6.5_linux_amd64.tar.gz /tmp/consul-template.tgz
RUN cd /bin && gzip -dc /tmp/consul-template.tgz | tar -xf - && rm /tmp/consul-template.tgz && mv /bin/consul-template_0.6.5_linux_amd64/consul-template /bin/consul-template && rmdir /bin/consul-template_0.6.5_linux_amd64

ENTRYPOINT ["/bin/consul-template"]
