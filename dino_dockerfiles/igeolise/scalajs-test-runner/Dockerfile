FROM igeolise/sbt:1.2.6-openjdk-8

ENV SBT_OPTS="-Xmx4g"

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get install -y --no-install-recommends bzip2 && \
    apt-get install -y --no-install-recommends xvfb && \
    apt-get install -y --no-install-recommends chromium-browser && \
    apt-get install -y --no-install-recommends unzip && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

RUN npm install jsdom@11.12.0

RUN curl -sS -o /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/2.25/chromedriver_linux64.zip && \
	mkdir /opt/google && \
	unzip -qq /tmp/chromedriver_linux64.zip -d /opt/google && \
	rm /tmp/chromedriver_linux64.zip && \
	chmod +x /opt/google/chromedriver && \
	ln -fs /opt/google/chromedriver /usr/local/bin/chromedriver
