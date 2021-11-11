FROM openjdk:8-jdk

USER root

RUN apt-get update
RUN apt-get install -y --no-install-recommends curl docker git mercurial iptables php php-curl

# install node
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get -y install nodejs
RUN npm install -g n
RUN n 6.9.2

# install yarn
RUN apt-get remove cmdtest
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends yarn

RUN mkdir /workspace && \
	chmod 777 /workspace

RUN curl -O https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/3.3/swarm-client-3.3.jar

RUN git clone https://github.com/phacility/libphutil.git /root/libphutil
RUN git clone https://github.com/phacility/arcanist.git /root/arcanist
ENV PATH "/root/arcanist/bin:${PATH}"

# install chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update
RUN apt-get install -y --no-install-recommends google-chrome-stable xvfb unzip

# install chromedriver
RUN wget -N http://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN chmod +x chromedriver
RUN mv -f chromedriver /usr/local/share/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
RUN ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

RUN echo 'kernel.unprivileged_userns_clone=1' > /etc/sysctl.d/00-local-userns.conf
RUN service procps restart

CMD echo "{\"hosts\": {\"$PHAB_HOST\": {\"token\": \"$PHAB_TOKEN\"}}}" > /root/.arcrc \
	&& chmod 600 /root/.arcrc \
	&& java \
  -jar \
  /swarm-client-3.3.jar \
  -master $MASTER \
  -username $USER \
  -password $PASSWORD \
  -executors 1
