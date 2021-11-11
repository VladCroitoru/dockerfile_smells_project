FROM redpointgames/phabricator

EXPOSE 80 443 22 24

COPY refine.sh /baseline
RUN /baseline/refine.sh

# CMD ["/bin/bash", "/app/init.sh"]
# CMD ["/bin/bash", "/baseline/refine.sh"]
