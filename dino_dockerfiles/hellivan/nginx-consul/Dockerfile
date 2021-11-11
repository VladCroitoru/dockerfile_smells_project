FROM nginx:1.13.8

ENV CONSUL_HOST consul
ENV CONSUL_PORT 8500

ENV TMPL_DIR /etc/ctmpl
ENV CONSUL_TEMPLATE_VERSION 0.18.1


ADD ./nginx.conf.ctmpl ${TMPL_DIR}/nginx.conf.ctmpl
ADD ./start.sh /root/start.sh


EXPOSE 80 443

VOLUME ${TMPL_DIR}

RUN apt-get update &&\
    apt-get install -y curl unzip &&\
    cd /tmp &&\
    curl https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-template.zip &&\
    unzip consul-template.zip &&\
    rm -f consul-template.zip &&\
    mv consul-template /usr/local/bin/ &&\
    apt-get purge --auto-remove -y curl unzip &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*
    


ENTRYPOINT ["sh", "/root/start.sh"]
