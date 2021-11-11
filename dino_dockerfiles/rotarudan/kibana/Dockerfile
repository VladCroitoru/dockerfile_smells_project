FROM docker.elastic.co/kibana/kibana:5.6.2

COPY docker-entrypoint.sh /
COPY signup-app.js /usr/share/kibana/
COPY kibana-routes.js /usr/share/kibana/

RUN kibana-plugin install https://github.com/e-ucm/kibana-time-plugin/releases/download/5.6.2/kibana.zip \
  && kibana-plugin install https://github.com/e-ucm/kibana/releases/download/5.6.2/vega_vis-0.3.1--for-Kibana-5.6.2.zip \
  && kibana-plugin install https://github.com/e-ucm/kibana-swimlane-vis/releases/download/5.6.2/kibana.zip \
  && kibana-plugin install https://github.com/e-ucm/tk-kibana-vis/releases/download/5.6.2/kibana.zip \
  && kibana-plugin install https://github.com/e-ucm/badges-vis/releases/download/5.6.2/kibana.zip

EXPOSE 5601
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/local/bin/kibana-docker"]

