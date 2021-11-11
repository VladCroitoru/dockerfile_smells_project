FROM node:17.0.1-buster
LABEL maintainer "David J. M. Karlsen <david@davidkarlsen.com>"
ENV SONAR_CLI_VERSION=4.6.2.2472 YARN_VERSION=1.22.17
ENV FFOX_DOWNLOAD_URL=https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64

RUN apt-get update && apt-get -y --no-install-recommends install wget apt-transport-https git gnupg vim less psmisc zip unzip net-tools libdbus-glib-1-2 gosu procps bzip2 ca-certificates libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
	sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
	apt-get update && \
	apt-get -y --no-install-recommends install google-chrome-stable libx11-xcb1 && \
	apt-get clean && \
	rm -rf /var/cache/apt && \
	ln -s /opt/google/chrome/chrome /usr/local/bin/chrome && \
	wget -q -O - "${FFOX_DOWNLOAD_URL}" |tar xjv -C /opt && \
	ln -s /opt/firefox/firefox /usr/local/bin/firefox && \
	yarn global add sonarqube-scanner@latest stylelint && \
	wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_CLI_VERSION}-linux.zip -O /tmp/sonar.zip && \
	mkdir -p /home/node/.sonar/native-sonar-scanner && \
	unzip /tmp/sonar.zip -d /home/node/.sonar/native-sonar-scanner && \
	rm /tmp/sonar.zip && \
	wget https://yarnpkg.com/downloads/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz -O -|tar xzvf - -C /opt && \
	ln -sf /opt/yarn-v${YARN_VERSION}/bin/yarn /usr/local/bin/yarn && \
	ln -sf /opt/yarn-v${YARN_VERSION}/bin/yarnpkg /usr/local/bin/yarnpkg && \
	git config --global user.name "Jenkins" && \
	git config --global user.email "fsjenkins@evry.com"

ENV 	NPM_REGISTRY=https://nexus.finods.com/nexus/repository/npm-all/ \
	CHROME_BIN=/usr/bin/google-chrome \
	NPM_CONFIG_PREFIX=/home/node/.npm-global \
	PATH="/opt/firefox:/home/node/.sonar/native-sonar-scanner/sonar-scanner-${SONAR_CLI_VERSION}-linux/jre/bin:${PATH}" \
	GOSU_USER="0:0" \
	GOSU_CHOWN="/home/node" \
	PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
	JAVA_HOME=/home/node/.sonar/native-sonar-scanner/sonar-scanner-${SONAR_CLI_VERSION}-linux/jre

RUN	npm set registry ${NPM_REGISTRY} && \
	yarn config set registry ${NPM_REGISTRY} && \
	chown -R node:node /home/node

COPY --chmod=a+x gosu-entrypoint.sh /
ENTRYPOINT ["/gosu-entrypoint.sh"]
