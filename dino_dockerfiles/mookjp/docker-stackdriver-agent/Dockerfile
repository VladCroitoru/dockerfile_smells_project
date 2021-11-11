FROM debian:wheezy
MAINTAINER mookjpy@gmail.com

# This Dockerfile followed this instruction:
# https://cloud.google.com/monitoring/agent/install-agent

RUN apt-get update -y && apt-get install -y curl
RUN curl -s -S -f -o /etc/apt/sources.list.d/stackdriver.list "https://repo.stackdriver.com/wheezy.list"
RUN curl -s -f https://app.stackdriver.com/RPM-GPG-KEY-stackdriver | apt-key add -
RUN apt-get -q update

# Install the agent package, without prompting for an API key.
RUN DEBIAN_FRONTEND=noninteractive \
            apt-get -y -q install stackdriver-agent \
            && rm -rf /var/lib/apt/lists/*

ENV API_KEY api_key_is_required

CMD /opt/stackdriver/stack-config --api-key=$API_KEY && \
    service stackdriver-agent start
