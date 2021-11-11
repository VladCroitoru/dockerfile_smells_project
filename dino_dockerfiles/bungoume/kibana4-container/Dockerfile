FROM kibana:4.5

RUN \
  kibana plugin --install elastic/sense && \
  kibana plugin --install elasticsearch/marvel/latest && \
  kibana plugin --install elasticsearch/graph/latest && \
  kibana plugin --install kibana/timelion && \
  kibana plugin -i tagcloud -u https://github.com/stormpython/tagcloud/archive/master.zip && \
  chown -R kibana:kibana /opt/kibana

EXPOSE 5601
