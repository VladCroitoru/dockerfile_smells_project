# Linux OS
FROM elasticsearch:2.4.0

# Maintainer
MAINTAINER lmangani <lorenzo.mangani@gmail.com>

RUN groupadd -r kibi && useradd -r -m -g kibi kibi

# Setup Packages & Permissions
RUN apt-get update && apt-get clean \
 && wget -O /dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 \
 && chmod +x /dumb-init \
 && curl -sL https://deb.nodesource.com/setup_4.x | bash - \
 && apt-get install -y nodejs \
 && /usr/share/elasticsearch/bin/plugin install https://github.com/elasticfence/siren-join/releases/download/2.4.0/siren-join-2.4.0.zip \
 && /usr/share/elasticsearch/bin/plugin install https://raw.githubusercontent.com/elasticfence/elasticsearch-http-user-auth/2.4/jar/elasticfence-2.4.0-SNAPSHOT.zip \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
 
RUN cd /opt && wget https://download.support.siren.solutions/kibi/community?file=kibi-4.5.3-5-linux-x64.zip -O kibi-4.5.3-5-linux-x64.zip\
 && unzip kibi-4.5.3-5-linux-x64.zip \
 && rm -rf /opt/kibi-4.5.3-5-linux-x64.zip \
 && mv kibi-4.5.3-5-linux-x64 kibi \
 && chown -R kibi:kibi /opt/kibi \
 && chown -R elasticsearch:elasticsearch /var/lib/elasticsearch/ 
 
RUN cd /opt/kibi \
 && ./bin/kibi plugin --install kaae -u https://github.com/elasticfence/kaae/releases/download/snapshot/kaae-latest.tar.gz \
 && ./bin/kibi plugin --install kibana-auth-plugin -u https://github.com/elasticfence/kibana-auth-plugin/releases/download/0.1.1/kauth-latest.tar.gz \
 && ./bin/kibi plugin --install kibrand -u https://github.com/elasticfence/kibrand/archive/0.4.5.zip \
 && ./bin/kibi plugin --install kbn_sankey_vis -u https://github.com/elasticfence/kbn_sankey_vis/releases/download/snapshot/kbn_sankey_vis.tar.gz \
 && ./bin/kibi plugin --install elastic/timelion \
 && ./bin/kibi plugin --install elastic/sense \
 && chown -R kibi:kibi /opt/kibi 
  
COPY entrypoint.sh /opt/
RUN chmod 755 /opt/entrypoint.sh
ENV PATH /opt/kibi/kibi/bin:$PATH

# Expose Default Port
EXPOSE 5601 5606
EXPOSE 9200
EXPOSE 9300
EXPOSE 8899

# Exec on start
ENTRYPOINT ["/dumb-init", "--"]
CMD ["/opt/entrypoint.sh"]
