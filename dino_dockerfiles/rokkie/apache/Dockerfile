FROM ubuntu:14.04

MAINTAINER Rocco Bruyn <rocco.bruyn@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Install packages
# Create necessary directories
# Remove apt cache
# Add servername to apache config
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y \
		nano \
		apache2 && \
	mkdir -p \
		/var/lock/apache2 \
		/var/run/apache2 && \
	rm -rf /var/lib/apt/lists/* && \
	sed -i "N;$!/Global configuration\n#/a \
		ServerName localhost" /etc/apache2/apache2.conf

# Add script that starts the server
ADD run.sh /bin/run.sh
RUN chmod +x /bin/run.sh

# Overwrite default index file 
ADD index.html /var/www/html/index.html

# Expose port 80 for web traffic
EXPOSE 80

# Execute script to start mysql server
CMD ["run.sh"]
