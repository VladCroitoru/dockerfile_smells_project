FROM alpine:3.6
MAINTAINER Miguel Gonzalez (migolo10@gmail.com)
RUN apk add --no-cache openssh-client bash curl

ENV CT_URL https://releases.hashicorp.com/consul-template/0.19.0/consul-template_0.19.0_linux_amd64.zip
RUN curl -O -L $CT_URL && \
    unzip -q consul-template_0.19.0_linux_amd64.zip && \
    rm consul-template_0.19.0_linux_amd64.zip && \
    mv consul-template /usr/local/bin && \
    chmod +x /usr/local/bin/consul-template

ENV NGINXHUP_URL https://github.com/migolo/dockernginxhup/releases/download/v1.1.0/dockernginxhup_alpine
RUN curl -O -L $NGINXHUP_URL && \
    mv dockernginxhup_alpine /usr/local/bin/dockernginxhup && \
    chmod +x /usr/local/bin/dockernginxhup

CMD ['/usr/local/bin/consul-template']
