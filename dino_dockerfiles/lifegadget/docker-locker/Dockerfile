FROM ubuntu:14.04
MAINTAINER LifeGadget <contact-us@lifegadget.co>
 
# Basic environment setup
ENV DEBIAN_FRONTEND noninteractive
ENV LOCKER_VERSION 0.0.1
RUN apt-get update \
	&& apt-get install -yqq vim wget curl git subversion sshpass \
	&& apt-get install -yqq nodejs npm \
	&& npm install -g bower \
	&& apt-get install -yqq php5 \
	&& echo `which php`
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin 
RUN ln -s /usr/local/bin/composer.phar /usr/local/bin/composer

# Add a nicer bashrc config
ADD https://raw.githubusercontent.com/lifegadget/bashrc/master/snippets/history.sh /etc/bash.history
ADD https://raw.githubusercontent.com/lifegadget/bashrc/master/snippets/color.sh /etc/bash.color
ADD https://raw.githubusercontent.com/lifegadget/bashrc/master/snippets/shortcuts.sh /etc/bash.shortcuts
RUN { \
		echo ""; \
		echo 'source /etc/bash.history'; \
		echo 'source /etc/bash.color'; \
		echo 'source /etc/bash.shortcuts'; \
	} >> /etc/bash.bashrc
	
# SpiderMonkey, jsawk, and resty
RUN apt-get install -y libmozjs-24-bin \
	&& ln -s /usr/bin/js24 /usr/local/bin/js \
	&& echo "export JS=/usr/local/bin/js" > /etc/jsawkrc \
	&& wget -O/usr/local/bin/jsawk http://github.com/micha/jsawk/raw/master/jsawk \
	&& wget -O/usr/local/bin/resty http://github.com/micha/resty/raw/master/resty \
	&& chmod +x /usr/local/bin/jsawk /usr/local/bin/resty \
	&& { \
		echo ""; \
		echo "source /usr/local/bin/resty -W 'http://localhost:8091/pools/default'"; \
		echo ""; \
	} >> /etc/bash.bashrc
	
# Setup SSH permissions
RUN mkdir -p /root/.ssh \ 
	&& ssh-keyscan bitbucket.org > /root/.ssh/known_hosts \
	&& ssh-keyscan github.com >> /root/.ssh/known_hosts \
	&& ssh-keygen -q -t rsa -N '' -f /root/.ssh/container-key \
	&& { \
		echo ""; \
		echo "IdentityFile /root/.ssh/id_rsa";  \
	} >> /etc/ssh/ssh_config
	
# Create directory structure for volume sharing
RUN mkdir -p /app \
	&& mkdir -p /app/data \
	&& mkdir -p /app/resources \
	&& mkdir -p /app/conf \
	&& ln -s /app/data /storage
VOLUME ["/storage"]

# Add bootstrapper and other resources
COPY resources/docker-locker /usr/local/bin/docker-locker
RUN chmod +x /usr/local/bin/docker-locker
COPY resources/locker.txt /app/resources/locker.txt
COPY resources/docker.txt /app/resources/docker.txt
	
ENTRYPOINT ["docker-locker"]
CMD	["about"]