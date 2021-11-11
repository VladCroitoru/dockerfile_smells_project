# Pull base image
FROM nginx:latest

MAINTAINER vi.nt <vi.nt@geekup.vn>

# Install consul-template
RUN apt-get update && apt-get install -y --no-install-recommends curl unzip
RUN curl -o /tmp/consul-template.zip https://releases.hashicorp.com/consul-template/0.15.0/consul-template_0.15.0_linux_amd64.zip && \
    unzip /tmp/consul-template.zip -d /usr/local/bin && \
    rm -v /etc/nginx/conf.d/* && \
	curl -SL http://stedolan.github.io/jq/download/linux64/jq > /usr/local/bin/jq && chmod u+x /usr/local/bin/jq

# Add nginx.conf && nginx template
ADD nginx.conf /etc/nginx/nginx.conf
ADD nginx.conf.ctmpl /etc/nginx/nginx.conf.ctmpl
ADD entrypoint.sh /entrypoint.sh

# Add boot script
ADD startup.sh restart.sh consul_config.sh config.json /
RUN chmod u+x /startup.sh && \
    chmod u+x /restart.sh && \
    chmod u+x /entrypoint.sh && \
    chmod u+x /consul_config.sh

# make /template directory and set it as volume for external template file
RUN mkdir /template
VOLUME /template

WORKDIR /

EXPOSE 80 443

# Set entrypoint.sh as entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
# Set statup.sh scripts as default cmd
CMD ["/startup.sh"]
