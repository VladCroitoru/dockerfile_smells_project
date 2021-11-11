FROM ubuntu
MAINTAINER Joseph M. "joe@teneleven.co.uk"
ENV DEBIAN_FRONTEND noninteractive

# Install base utilities
RUN apt-get -y update && apt-get -y -q install wget ca-certificates

# Prepare sources
RUN wget -q -O - "https://dl-ssl.google.com/linux/linux_signing_key.pub" | apt-key add -
RUN echo "deb http://security.ubuntu.com/ubuntu precise-security main" >> /etc/apt/sources.list
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list
RUN apt-get -y update

# Install utilities from sources
RUN apt-get -y install libnss3-1d dbus dpkg openjdk-7-jre google-chrome-stable xvfb unzip apparmor-utils
RUN apt-get -y update

# # Download and copy the ChromeDriver to /usr/local/bin
RUN cd /tmp
RUN wget "http://chromedriver.storage.googleapis.com/2.15/chromedriver_linux64.zip"
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin
RUN wget "http://selenium-release.storage.googleapis.com/2.45/selenium-server-standalone-2.45.0.jar"
RUN mv selenium-server-standalone-2.45.0.jar /usr/local/bin
ADD files /

# Forward ports
EXPOSE 4444 9222

CMD ["/usr/local/bin/start-selenium-server.sh"]
