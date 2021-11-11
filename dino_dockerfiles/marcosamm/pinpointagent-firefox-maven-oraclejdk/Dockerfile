# DESCRIPTION       Pinpoint APM Agent + firefox + maven + oraclejdk
# TO_BUILD          docker build -t pinpoint-agent .
# TO_RUN            docker run --name=pinpoint-agent pinpoint-agent
# or
# TO_RUN            docker run -it \
#                       -e COLLECTOR_IP="192.168.0.18" \
#                       -e PROFILER_APPLICATIONSERVERTYPE="TOMCAT" \
#                       -e PROFILER_TOMCAT_CONDITIONAL_TRANSFORM="false" \
#                       -e PROFILER_SAMPLING_RATE="1" \
#                       -e PROFILER_JSON_JSONLIB="true" \
#                       -e PROFILER_JSON_JACKSON="true"\
#                       -e PROFILER_JSON_GSON="true" \
#                       pinpoint-agent

FROM persapiens/firefox-maven-oraclejdk:56-3.5.0-8u152
MAINTAINER Marcos Alexandre de Melo Medeiros <marcosamm@gmail.com>

ENV PINPOINT_VERSION 1.6.2
ENV PINPOINT_AGENT_HOME /opt/pinpoint-agent

RUN apt-get update -qqy && \
  apt-get upgrade -qqy --no-install-recommends && \
  apt-get install -qqy curl unzip && \
  mkdir -p $PINPOINT_AGENT_HOME && \
  curl -fsSL https://github.com/naver/pinpoint/releases/download/$PINPOINT_VERSION/pinpoint-agent-$PINPOINT_VERSION.tar.gz \
  | tar -xzC $PINPOINT_AGENT_HOME && \
  cd $PINPOINT_AGENT_HOME && \
  mv pinpoint-bootstrap-$PINPOINT_VERSION.jar pinpoint-bootstrap.jar && \
  curl -o /usr/local/bin/configure-agent.sh -fsSL https://raw.githubusercontent.com/marcosamm/docker-pinpoint/master/pinpoint-agent/configure-agent.sh && \
  chmod +x /usr/local/bin/configure-agent.sh && \
  apt-get remove --purge --auto-remove -y curl unzip && \
  apt-get autoclean && apt-get --purge -y autoremove && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/*

ENTRYPOINT ["/usr/local/bin/configure-agent.sh"]
CMD ["bash"]