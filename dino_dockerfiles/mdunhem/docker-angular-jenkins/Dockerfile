FROM node:8

ARG ANGULAR_CLI_VERSION=1.2.3
ARG GID=988
ARG UID=406

LABEL maintainer="Mikael Dunhem <mikael.dunhem@gmail.com>"
LABEL node_version=${NODE_VERSION}
LABEL angular_cli_version=${ANGULAR_CLI_VERSION}
LABEL chrome_version="stable"

USER root

# Install chrome for testing
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y Xvfb google-chrome-stable && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install rsync
RUN apt-get update && apt-get install -y rsync

# Start xvfb and chrome (in no-sandbox mode)
ADD xvfb-chrome.sh /usr/bin/xvfb-chrome
RUN ln -sf /usr/bin/xvfb-chrome /usr/bin/google-chrome
RUN chmod 755 /usr/bin/google-chrome

# Export chome stuff for karma tests
ENV CHROME_BIN /usr/bin/google-chrome

#### Hack to get by Jenkins not properly starting the docker image ###
RUN groupadd -g ${GID} jenkins
RUN useradd -u ${UID} -g ${GID} -G root -m jenkins

USER jenkins

RUN mkdir /home/jenkins/.npm-global
ENV NPM_CONFIG_PREFIX=/home/jenkins/.npm-global
ENV PATH=/home/jenkins/.npm-global/bin:$PATH
######################################################################

# Install angular cli globally
RUN npm install -g @angular/cli@${ANGULAR_CLI_VERSION}
