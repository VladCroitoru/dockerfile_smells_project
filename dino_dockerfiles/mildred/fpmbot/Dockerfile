FROM debian:stable
VOLUME ["/var/lib/fpmbot"]
RUN	apt-get update; \
	DEBIAN_FRONTEND=noninteractive apt-get install -y \
		rubygems inotify-tools daemontools dpkg-dev ruby-dev bzip2 git make; \
	gem install specific_install; gem specific_install https://github.com/mildred/fpm.git; \
	apt-get clean
COPY run /services/fpmbot/run 
COPY ssh-wrapper /services/fpmbot/ssh-wrapper
COPY log /services/fpmbot/log/run 
COPY fpmbot /usr/bin/fpmbot
RUN 	chmod 755 /usr/bin/fpmbot; \
	chmod 755 /services/fpmbot/run; \
	chmod 755 /services/fpmbot/ssh-wrapper; \
	chmod 755 /services/fpmbot/log/run
VOLUME ["/var/lib/fpmbot", "/var/log/fpmbot"]
CMD ["/usr/bin/svscan", "/services"]

