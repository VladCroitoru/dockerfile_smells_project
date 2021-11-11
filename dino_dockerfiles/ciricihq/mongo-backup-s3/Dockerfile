FROM ubuntu:16.04

# Install Python
RUN apt-get update && \
    apt-get -y install python python-pip wget zip

# Install AWS CLI and schedule package
RUN pip install awscli schedule

# Install MongoDB tools
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | \
    tee /etc/apt/sources.list.d/mongodb-org-3.2.list
RUN apt-get update && \
    apt-get install -y mongodb-org-tools

RUN wget -O /tmp/envconsul.zip https://releases.hashicorp.com/envconsul/0.6.2/envconsul_0.6.2_linux_amd64.zip
RUN unzip /tmp/envconsul.zip -d /tmp
RUN mv /tmp/envconsul /usr/bin/envconsul

# Add scripts
ADD backup.sh /app/backup.sh
ADD run.py /app/run.py
ADD consul-entrypoint.sh /app/consul-entrypoint.sh
RUN chmod +x /app/backup.sh
RUN chmod +x /app/run.py

# Default environment variables
ENV BACKUP_INTERVAL 1
ENV BACKUP_TIME 2:00
ENV DATE_FORMAT %Y%m%d-%H%M%S
ENV FILE_PREFIX backup-

# Run the schedule command on startup
CMD ["/app/consul-entrypoint.sh"]
