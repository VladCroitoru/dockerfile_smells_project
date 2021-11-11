FROM joshhsoj1902/docker-ogpagent:latest@sha256:e3a1604f953220017b0e83ec7e0bcf6a219a69aa23523de87de51e0b1bd9608e

ENV OGP_LISTEN_PORT=12679
ENV OGP_GAME_DIR=/opt/games/

RUN apt-get update \
 && apt-get install -y software-properties-common \
                       python-software-properties \
                       apt-transport-https \
                       ca-certificates \
                       curl \
                       software-properties-common \
                       netcat

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
 && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" \
 && apt-get update \
 && apt-cache policy docker-ce \
 && apt-get install -y  docker-ce

RUN sudo usermod -aG docker ogp_agent

ADD ogpmanager.sh /usr/local/bin/
RUN mv /usr/local/bin/ogpmanager.sh /usr/local/bin/ogpmanager \
    && chmod +x /usr/local/bin/ogpmanager

RUN curl -sSLf -z /usr/local/bin/gomplate -o /usr/local/bin/gomplate https://github.com/hairyhenderson/gomplate/releases/download/v3.0.0/gomplate_linux-amd64-slim \
  && chmod 755 /usr/local/bin/gomplate

COPY templates /opt/OGP/templates

RUN chown -R ogp_agent:ogp_agent /opt/OGP/ \
 && rm -rf /opt/agent

COPY OGP-Agent-Linux /opt/OGP

RUN chown -R ogp_agent:ogp_agent /opt/OGP/ \
 && chmod 777 /opt

# Ideally this wouldn't be here... but for now it's easy
COPY tests /tests
RUN apt-get install -y vim

HEALTHCHECK CMD ./docker-health.sh
