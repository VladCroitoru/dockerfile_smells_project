FROM shashikant86/docker-bdd

MAINTAINER Abdulkadir Yaman <abdulkadiryaman@gmail.com>

RUN wget --no-check-certificate -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - 
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN sh -c 'echo "deb http://packages.linuxmint.com debian import" >> /etc/apt/sources.list'

RUN apt-get update 

RUN DEBIAN_FRONTEND=noninteractive \
	apt-get install -y --force-yes \
	ca-certificates \
	fonts-takao \
	gconf-service \
	gksu \
	libappindicator1 \
	libasound2 \
	libcurl3 \
	libgconf-2-4 \
	libnspr4 \
	libnss3 \
    	libxss1 \
	libpango1.0-0 \
    	build-essential \
    	chrpath \
    	libssl-dev \
    	libxft-dev \
    	libfreetype6 \
    	libfreetype6-dev \
    	libfontconfig1 \
    	libfontconfig1-dev \
	pulseaudio \
	python-psutil \
	supervisor \
	wget \
	xbase-clients \
	xdg-utils \
	xvfb \
    	firefox \
    	freetds-dev \
    	cowsay \
    	zlib1g-dev \
    	qt5-default \
    	qt5-qmake \
    	libqt5webkit5-dev \
    	unzip \
	google-chrome-stable 

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN ln -s /lib/x86_64-linux-gnu/libudev.so.1 /lib/x86_64-linux-gnu/libudev.so.0

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

VOLUME ["/home/chrome"]

RUN useradd -m -G pulse-access chrome

### installing chrome driver
RUN wget --no-check-certificate -N https://chromedriver.storage.googleapis.com/2.15/chromedriver_linux64.zip -P /tmp/
RUN unzip /tmp/chromedriver_linux64.zip -d /tmp
RUN chmod +x /tmp/
RUN ls -altrh /tmp/chromedriver
RUN mv /tmp/chromedriver /usr/bin/
### installing chrome driver END

ENV LANG en_US.UTF-8

COPY Gemfile* /tmp/
WORKDIR /tmp
RUN bundle install --verbose

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
