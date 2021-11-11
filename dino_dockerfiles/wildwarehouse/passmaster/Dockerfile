FROM fedora:25
COPY run.sh entrypoint.sh config known_hosts post-commit.sh /opt/docker/
RUN ["/usr/bin/sh", "/opt/docker/run.sh"]
ENTRYPOINT ["/usr/bin/sh", "/opt/docker/entrypoint.sh"]