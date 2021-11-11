FROM zeroc0d3lab/centos-base:latest
MAINTAINER ZeroC0D3 Team <zeroc0d3.team@gmail.com>

#-----------------------------------------------------------------------------
# Set Environment
#-----------------------------------------------------------------------------
ENV CONSULTEMPLATE_VERSION=0.19.3

#-----------------------------------------------------------------------------
# Set Group & User for 'consul'
#-----------------------------------------------------------------------------
RUN mkdir -p /var/lib/consul \
    && groupadd consul \
    && useradd -r -g consul consul \
    && usermod -aG consul consul \
    && chown -R consul:consul /var/lib/consul

#-----------------------------------------------------------------------------
# Install Consul Template Library
#-----------------------------------------------------------------------------
RUN curl -sSL https://releases.hashicorp.com/consul-template/${CONSULTEMPLATE_VERSION}/consul-template_${CONSULTEMPLATE_VERSION}_linux_amd64.zip -o /opt/consul-template.zip \
    && unzip /opt/consul-template.zip -d /bin \
    && rm -f /opt/consul-template.zip

#-----------------------------------------------------------------------------
# Setup TrueColors (Terminal)
#-----------------------------------------------------------------------------
COPY ./rootfs/root/colors/24-bit-color.sh /opt/24-bit-color.sh
RUN chmod a+x /opt/24-bit-color.sh; sync \
    && sudo /bin/sh /opt/24-bit-color.sh

#-----------------------------------------------------------------------------
# Set PORT Docker Container
#-----------------------------------------------------------------------------
EXPOSE 2220

#-----------------------------------------------------------------------------
# Finalize (reconfigure)
#-----------------------------------------------------------------------------
COPY rootfs/ /

#-----------------------------------------------------------------------------
# Cleanup 'root', 'opt' & 'tmp' folder
#-----------------------------------------------------------------------------
RUN rm -f /root/*.tar.gz \
    && rm -f /root/*.zip \
    && rm -f /opt/*.tar.gz \
    && rm -f /opt/*.zip \
    && rm -f /tmp/*.tar.gz \
    && rm -f /tmp/*.zip     

#-----------------------------------------------------------------------------
# Check Docker Container
#-----------------------------------------------------------------------------
# HEALTHCHECK CMD [ $(curl -sI -w '%{http_code}' --out /dev/null http://localhost:8500/v1/agent/self) == "200" ] || exit 1
HEALTHCHECK CMD --interval=5m --timeout=3s /etc/cont-consul/check || exit 1