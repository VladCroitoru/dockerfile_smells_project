FROM jmoger/gitblit:1.5.1

MAINTAINER Rushan Pun, <rushan.pun@accenture.com>

USER root
COPY gitblit-entrypoint.sh /
RUN chmod +x /gitblit-entrypoint.sh

# Run entrypoint script
ENTRYPOINT ["/gitblit-entrypoint.sh"]

# Setup the Docker container environment and run Gitblit
workdir /opt/gitblit

expose 9000
cmd ["java", "-server", "-Xmx1024M", "-Djava.awt.headless=true", "-jar", "/opt/gitblit/gitblit.jar", "--baseFolder", "/opt/gitblit-data"]

