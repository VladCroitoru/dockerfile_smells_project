### QNIBTerminal debian image
FROM qnib/d-supervisor

ENV TERM=xterm \
    BOOTSTRAP_CONSUL=false \
    RUN_SERVER=false \
    CONSUL_VER=0.7.1 \
    CT_VER=0.16.0 \
    QNIB_CONSUL=0.1.3.4
RUN apt-get update && \
    apt-get install -y bsdtar curl jq bc
RUN curl -fsL https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_linux_amd64.zip | bsdtar xf - -C /usr/local/bin/ && \
    chmod +x /usr/local/bin/consul
RUN mkdir -p /opt/consul-web-ui/ && \
    curl -fsL http://dl.bintray.com/mitchellh/consul/${CONSUL_VER}_web_ui.zip | bsdtar xf - -C /opt/consul-web-ui/ && \
    unset CONSUL_VER
RUN curl -Lsf https://releases.hashicorp.com/consul-template/${CT_VER}/consul-template_${CT_VER}_linux_amd64.zip | bsdtar xf - -C /usr/local/bin/ && \
    chmod +x /usr/local/bin/consul-template && \
    unset CT_VER
RUN wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.2.2/go-github_0.2.2_Linux \
 && chmod +x /usr/local/bin/go-github \
 && echo "# consul-content: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo consul-content --regex ".*\.tar" --limit 1)" \
 && curl -fsL $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo consul-content --regex ".*\.tar" --limit 1) |tar xf - -C /opt/qnib/ \
 && echo "consul members" >> /root/.bash_history

ADD etc/consul.d/agent.json /etc/consul.d/
ADD etc/supervisord.d/consul.ini /etc/supervisord.d/
