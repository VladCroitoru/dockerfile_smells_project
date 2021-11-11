FROM qnib/alpn-supervisor

ARG CONSUL_VER=0.7.5
ARG CT_VER=0.18.5
ENV DOCKER_HOST=tcp://172.17.0.1:2376

RUN apk add --no-cache curl unzip nmap bc jq curl ca-certificates openssl \
 && curl -fso /tmp/consul.zip https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_linux_amd64.zip \
 && mkdir -p /opt/qnib/consul/bin/ \
 && cd /opt/qnib/consul/bin/ \
 && unzip /tmp/consul.zip \
 && ln -s /opt/qnib/consul/bin/consul /usr/local/bin/ \
 && rm -f /tmp/consul.zip \
 && mkdir -p /opt/consul-web-ui \
 && curl -Lso /tmp/consul-web-ui.zip https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_web_ui.zip \
 && cd /opt/consul-web-ui \
 && unzip /tmp/consul-web-ui.zip \
 && rm -f /tmp/consul-web-ui.zip \
 && curl -Lso /tmp/consul-template.zip https://releases.hashicorp.com/consul-template/${CT_VER}/consul-template_${CT_VER}_linux_amd64.zip \
 && cd /opt/qnib/consul/bin/ \
 && ln -s /opt/qnib/consul/bin/consul-template /usr/local/bin/ \
 && unzip /tmp/consul-template.zip \
 && rm -f /tmp/consul-template.zip \
 && wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.2.2/go-github_0.2.2_MuslLinux \
 && chmod +x /usr/local/bin/go-github \
 && echo "# consul-content: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo consul-content --regex ".*\.tar" --limit 1)" \
 && curl -fsL $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo consul-content --regex ".*\.tar" --limit 1) |tar xf - -C /opt/qnib/ \
 && apk --no-cache del unzip \
 && wget -qO /usr/local/bin/go-getmyname $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo go-getmyname --regex ".*alpine" --limit 1) \
 && chmod +x /usr/local/bin/go-getmyname \
 && rm -f /tmp/consul-template.zip \
 && wget -qO - $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo consul-cli --regex ".*alpine" --limit 1) |tar xfz - -C /tmp/ \
 && mv /tmp/consul-cli_*_alpine/consul-cli /usr/local/bin/ \
 && echo "consul members" >> /root/.bash_history
ADD etc/consul.d/agent.json \
    etc/consul.d/consul.json \
    /etc/consul.d/
ADD etc/supervisord.d/consul.ini /etc/supervisord.d/
