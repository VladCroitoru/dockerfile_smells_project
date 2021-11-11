# Version
 FROM grafana/grafana:latest
#FROM grafana/grafana:3.1.1

# Re-Install curl for the dashboard setup
RUN apt-get update && \
    apt-get -y --no-install-recommends install curl && \
    apt-get clean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Copy in bootstrapping script
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

ENTRYPOINT ["/bin/bash"]
CMD ["/docker-entrypoint.sh"]
