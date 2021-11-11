### QNIBTerminal ubuntu image
FROM qnib/u-supervisor

ENV TERM=xterm \
    BOOTSTRAP_CONSUL=false \
    RUN_SERVER=false
ARG CONSUL_VER=0.6.4
ARG CT_VER=0.15.0 
ARG DUMB_INIT_VER=1.1.1

RUN apt-get update \
 && apt-get install -y bsdtar curl iproute wget \
 && curl -fsL https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_linux_amd64.zip | bsdtar xf - -C /usr/local/bin/ \
 && chmod +x /usr/local/bin/consul \
 && mkdir -p /opt/consul-web-ui/ \
 && curl -fsL https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_web_ui.zip |bsdtar xf - -C /opt/consul-web-ui/ \
 && unset CONSUL_VER \
 && curl -Lsf https://releases.hashicorp.com/consul-template/${CT_VER}/consul-template_${CT_VER}_linux_amd64.zip |bsdtar xf - -C /usr/local/bin/ \
 && chmod +x /usr/local/bin/consul-template \
 && unset CT_VER \
 && wget -qO /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VER}/dumb-init_${DUMB_INIT_VER}_amd64 \
 && chmod +x /usr/local/bin/dumb-init \
 && wget -qO /usr/local/bin/go-github https://github.com/qnib/go-github/releases/download/0.2.2/go-github_0.2.2_Linux \
 && chmod +x /usr/local/bin/go-github \
 && echo "# consul-content: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo consul-content --regex ".*\.tar" --limit 1)" \
 && curl -fsL $(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo consul-content --regex ".*\.tar" --limit 1) |tar xf - -C /opt/qnib/ 
ADD etc/supervisord.d/consul.ini /etc/supervisord.d/
ADD etc/consul.d/agent.json \
    etc/consul.d/consul.json \
    /etc/consul.d/
