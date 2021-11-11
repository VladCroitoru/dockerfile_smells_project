FROM registry.gitlab.com/shimaore/docker.opensips:v5.0.0-rebuild
MAINTAINER Stéphane Alnet <stephane@shimaore.net>
ENV NODE_ENV production

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates \
  curl \
  git \
  make \
  && \
  git clone https://github.com/tj/n.git n.git && \
  cd n.git && \
  make install && \
  cd .. && \
  rm -rf n.git && \
  n 12.4.0

# Start opensips part.
COPY . /home/opensips
RUN chown -R opensips.opensips /home/opensips
USER opensips
WORKDIR /home/opensips

RUN mkdir -p log run/opensips \
  && npm install && npm cache -f clean \
  && npm run prepare

USER root
RUN \
  apt-get purge -y \
    build-essential \
    ca-certificates \
    cpp-8 \
    gcc-8 \
    curl \
    git \
    make \
  && apt-get autoremove -y \
  && apt-get clean

USER opensips
# 5060: default proxy_port for `client` profile
# 5070: default proxy_port for `registrant` profile
# 8560: httpd_port (MI-JSON interface)
EXPOSE 5060 5060/udp 5070 5070/udp 8560
CMD ["npm","start"]
