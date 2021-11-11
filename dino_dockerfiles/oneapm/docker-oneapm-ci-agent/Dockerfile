FROM debian:jessie

MAINTAINER Cloudinsight <package@oneapm.com>

ENV AGENT_VERSION 1:4.7.3-1

# Install the Agent
RUN echo "deb http://apt.oneapm.com/ stable main" > /etc/apt/sources.list.d/cloudinsight-agent.list \
 && apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 62C7DA6D \
 && apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 B421195B \
 && apt-get update \
 && apt-get install --no-install-recommends -y cloudinsight-agent="${AGENT_VERSION}" \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Configure the Agent
# 1. Turn syslog off
# 2. Remove cloudinsight-agent user from supervisor configuration
# 3. Remove cloudinsight-agent user from init.d configuration
# 4. Fix permission on /etc/init.d/cloudinsight-agent
# 5. Remove network check
RUN mv /etc/cloudinsight-agent/cloudinsight-agent.conf.example /etc/cloudinsight-agent/cloudinsight-agent.conf \
 && sed -i -e"s/^.*log_to_syslog:.*$/log_to_syslog: no/" /etc/cloudinsight-agent/cloudinsight-agent.conf \
 && sed -i "/user=cloudinsight-agent/d" /etc/cloudinsight-agent/supervisord.conf \
 && sed -i 's/AGENTUSER="cloudinsight-agent"/AGENTUSER="root"/g' /etc/init.d/cloudinsight-agent \
 && chmod +x /etc/init.d/cloudinsight-agent \
 && rm /etc/cloudinsight-agent/conf.d/network.yaml.default

# Add Docker check
COPY conf.d/docker_daemon.yaml /etc/cloudinsight-agent/conf.d/docker_daemon.yaml

COPY entrypoint.sh /entrypoint.sh

# Extra conf.d and checks.d
VOLUME ["/conf.d"]
VOLUME ["/checks.d"]

# Expose StatsD port
EXPOSE 8251/udp

ENTRYPOINT ["/entrypoint.sh"]
CMD ["supervisord", "-n", "-c", "/etc/cloudinsight-agent/supervisord.conf"]
