FROM kibana:latest
RUN gosu kibana kibana plugin --install elastic/sense
RUN gosu kibana kibana plugin --install elasticsearch/marvel/latest
RUN gosu kibana kibana plugin --install stormpython/tagcloud
RUN gosu kibana kibana plugin --install sirensolutions/kibi-radar-chart-plugin/0.1.0
