FROM ido4pro/tineco-esp8266-toolchain-docker

# ------------------------------------------------------------------------------	
# Install Node
# ------------------------------------------------------------------------------

RUN apt-get update

RUN apt-get install -y curl

RUN set -ex \
  && for key in \
    9554F04D7259F04124DE6B476D5A82AC7E37093B \
    94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
    0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
    FD3A5288F042B6850C66B31F09FE44734EB7990E \
    71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
    DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    B9AE9905FFD7803F25714661B63B535A4C206CA9 \
    C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
  ; do \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
  done

ENV NPM_CONFIG_LOGLEVEL info
ENV NODE_VERSION 4.4.7

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz"
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc"
RUN gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc
RUN grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c -
RUN tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1
RUN rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt

# ------------------------------------------------------------------------------
# Install Cloud9
# ------------------------------------------------------------------------------

RUN git clone https://github.com/c9/core.git /opt/cloud9
WORKDIR /opt/cloud9
RUN scripts/install-sdk.sh

# Install all the required dependencies
RUN curl -L https://raw.githubusercontent.com/c9/install/master/install.sh | bash

# ------------------------------------------------------------------------------
# Tweak standlone.js conf
# ------------------------------------------------------------------------------

RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /opt/cloud9/configs/standalone.js 

# ------------------------------------------------------------------------------
# Install Supervisor.
# ------------------------------------------------------------------------------

RUN apt-get install -y supervisor
RUN sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

# ------------------------------------------------------------------------------
# Add supervisord configs
# ------------------------------------------------------------------------------

ADD conf/* /etc/supervisor/conf.d/

# ------------------------------------------------------------------------------
# Clean up APT when done.
# ------------------------------------------------------------------------------

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


EXPOSE 80

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
