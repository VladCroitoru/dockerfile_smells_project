FROM kibana

RUN kibana plugin --install elasticsearch/marvel/latest

RUN chown -R kibana:kibana /opt/kibana

EXPOSE 5601
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["kibana"]
