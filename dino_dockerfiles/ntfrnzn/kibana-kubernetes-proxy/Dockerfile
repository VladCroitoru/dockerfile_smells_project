FROM kibana:4.5

USER kibana
COPY kibana.yml /opt/kibana/config
RUN timeout 120 kibana || true
USER root

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["kibana"]
