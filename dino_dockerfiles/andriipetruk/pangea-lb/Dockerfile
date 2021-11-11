FROM centos:centos6

MAINTAINER Andrii Petruk <andrey.petruk@gmail.com>


ENV CONSUL_TEMPLATE_VERSION=0.10.0
#OPENAM_URL=http://openam:8080/openam AGENT_PROFILE_NAME=WebAgent AGENT_PASSWORD=password CONFIRM=y

ENV LUAJIT_VERSION=2.0.3 \
    LUAJIT_MAJOR_VERSION=2.0 \
    LUAJIT_LIB=/usr/local/lib \
    LUACJSON_VERSION=2.1.0 \
    LUA_INCLUDE_DIR=/usr/local/include/luajit-2.0 \
    LUAINC=/usr/local/include/luajit-2.0 \
    LUAJIT_INC=/usr/local/include/luajit-2.0

RUN yum -y install unzip tar file gcc  gcc-c++  zlib-devel nspr-devel nss-devel libxml2-devel pcre-devel openssl-dev wget && \
    ln -s /lib64/libpcre.so.0 /lib64/libpcre.so.1 && \
    ln -s /usr/lib64/libcrypto.so.10 /usr/lib64/libcrypto.so && \
    ln -s /usr/lib64/libssl.so.10 /usr/lib64/libssl.so

RUN  cd /tmp && \
     wget http://luajit.org/download/LuaJIT-${LUAJIT_VERSION}.tar.gz && \
     tar xvf LuaJIT-${LUAJIT_VERSION}.tar.gz && \
     make install --directory=/tmp/LuaJIT-${LUAJIT_VERSION} && \
     ln -s /usr/local/lib/libluajit-5.1.so.2 /lib64/libluajit-5.1.so.2 && \
     wget http://www.kyne.com.au/~mark/software/download/lua-cjson-${LUACJSON_VERSION}.tar.gz && \
     tar xvf lua-cjson-${LUACJSON_VERSION}.tar.gz && \
     make --directory=/tmp/lua-cjson-${LUACJSON_VERSION} LUA_INCLUDE_DIR=$LUA_INCLUDE_DIR && \
     make install --directory=/tmp/lua-cjson-${LUACJSON_VERSION}


ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /

RUN unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    mv consul-template /usr/local/bin/consul-template &&\
    rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    mkdir -p /consul-template /consul-template/config.d /consul-template/templates


RUN mkdir -p /etc/nginx /tmp/nginx /defaults /etc/nginx/templates

ADD defaults/ /defaults
ADD scripts /scripts/

COPY nginx_Linux_64_agent_4.0.0-SNAPSHOT.zip /tmp

RUN unzip /tmp/nginx_Linux_64_agent_4.0.0-SNAPSHOT.zip -d /opt && \
    mv /opt/web_agents/nginx_agent /opt/nginx_agent && rm -rf /opt/web_agents \
    rm /tmp/nginx_Linux_64_agent_4.0.0-SNAPSHOT.zip \
    rm -rf /opt/nginx_agent/html \
    rm /opt/nginx_agent/conf/nginx.conf \


COPY OpenSSOAgentConfiguration.properties /opt/nginx_agent/conf/OpenSSOAgentConfiguration.properties 

ADD  error /opt/nginx_agent/error
COPY nginx.tmpl /consul-template/templates/
COPY consul.cfg /consul-template/config.d/

CMD ["/scripts/launch.sh"]
#CMD [ "/usr/local/bin/consul-template"]
