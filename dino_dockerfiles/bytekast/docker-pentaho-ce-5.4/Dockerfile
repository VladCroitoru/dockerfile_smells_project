FROM bytekast/docker-pentaho-base

MAINTAINER Rowell Belen developer@bytekast.com

# Install useful command line utilities
RUN apt-get install -y man vim sudo
RUN apt-get install -y zip unzip

# Postgres AUFS bug hack
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/; rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R 0700 /etc/ssl/private; chown -R postgres /etc/ssl/private

# Download and extract pentaho BA Server binary
WORKDIR /home/pentaho/
RUN wget http://iweb.dl.sourceforge.net/project/pentaho/Business%20Intelligence%20Server/5.4/biserver-ce-5.4.0.0-128.zip
RUN unzip biserver-ce-5.4.0.0-128.zip -d biserver-ce-5.4.0.0-128
RUN rm biserver-ce-5.4.0.0-128.zip

# Add/run script to load default tables
ADD loaddb.sh /home/pentaho/
RUN chmod +x /home/pentaho/loaddb.sh
RUN /etc/init.d/postgresql start && \
	printf 'password\n' | /home/pentaho/loaddb.sh

# Add script to start biserver
ADD start.sh /home/pentaho/
RUN chmod +x /home/pentaho/start.sh

# Redirect Tomcat output
ENV CATALINA_OUT /dev/stdout

# Start Service
EXPOSE 8080 22 5432
CMD /home/pentaho/start.sh && /usr/bin/supervisord

