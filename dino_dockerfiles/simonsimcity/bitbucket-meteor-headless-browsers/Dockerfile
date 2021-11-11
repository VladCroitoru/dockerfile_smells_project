FROM simonsimcity/bitbucket-meteor:1.6

USER root

# Install curl, bzip2, git, libfontconfig (an undocumented dependency of phantomjs) and build-tools
RUN apt-get update && \
    apt-get install -y xvfb default-jre && \
    rm -rf /var/lib/apt/lists/*

# Install Firefox 45.4.0 (https://github.com/SeleniumHQ/selenium/blob/master/java/CHANGELOG#L33)
RUN curl -o /var/tmp/firefox-45.4.0esr.tar.bz2 https://ftp.mozilla.org/pub/firefox/releases/45.4.0esr/linux-x86_64/en-US/firefox-45.4.0esr.tar.bz2 && \
	tar xvfj /var/tmp/firefox-45.4.0esr.tar.bz2 && \
	rm /var/tmp/firefox-45.4.0esr.tar.bz2 && \
	ln -s /firefox/firefox-bin /usr/bin/firefox

# Install Chromium and register as Chrome
RUN apt-get update && \
    apt-get install -y chromium-browser && \
    rm -rf /var/lib/apt/lists/*
ADD chrome-nosandbox /usr/bin/chrome
RUN chmod +x /usr/bin/chrome

USER meteor
