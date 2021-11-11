FROM ubuntu:latest

# Install Haproxy.
RUN \
  apt-get update && \
  apt-get install -y python python-setuptools haproxy && \
  sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy && \
  rm -rf /var/lib/apt/lists/*

# Install Edgerouter deps
RUN easy_install requests==2.7.0

# Add files.
ADD edgerouter.py /usr/bin/edgerouter.py
ADD haproxy.cfg /etc/haproxy/haproxy.cfg
ADD start.bash /haproxy-start

# configure edgerouter.py into a cron job that runs every minute
# Add crontab file in the cron directory
RUN echo '* * * * * root /usr/bin/edgerouter.py -m $(cat /etc/marathon.hosts)' >> /etc/cron.d/edgerouter-cron
RUN echo '# Dont remove the empty line at the end of this file. It is required to run the cron job' >> /etc/cron.d/edgerouter-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/edgerouter-cron
 
# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Define mountable directories.
VOLUME ["/haproxy-override"]

# Define working directory.
WORKDIR /etc/haproxy

# Define default command.
CMD "echo ${MARATHON_HOSTS} > /etc/marathon.hosts && cron && /haproxy-start"

# Expose ports.
EXPOSE 80
EXPOSE 443
