# Linux OS
FROM elasticsearch:2.1.2

# Maintainer
MAINTAINER zorino <maximilien1er@gmail.com>

# Install dependencies and kibi
RUN apt-get update && apt-get clean \
 && curl -sL https://deb.nodesource.com/setup_4.x | bash - \
 && apt-get install -y nodejs \
 && cd /opt && wget http://bit.do/kibi-0-3-0-linux-x64-zip \
 && unzip kibi-0-3-0-linux-x64-zip \
 && ln -s kibi-0.3.0-linux-x64 kibi \
 && /usr/share/elasticsearch/bin/plugin install solutions.siren/siren-join/2.1.2

# Entrypoint
COPY entrypoint.sh /opt/entrypoint.sh
RUN chmod 755 /opt/entrypoint.sh
ENTRYPOINT ["/opt/entrypoint.sh"]
# ENTRYPOINT ["tail", "-f", "/dev/null"]

# Expose Default Port
EXPOSE 9200 9300 5601
