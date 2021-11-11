FROM golang:onbuild
# Install Goose, the DB migration tool
RUN go get bitbucket.org/liamstask/goose/cmd/goose

# Silencing "debconf: unable to initialize frontend: Dialog" warnings
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Install Vim text editor
RUN apt-get update && apt-get install -y apt-utils && apt-get install -y vim

# Install Crontab
RUN apt-get install -y cron

# Setup Logging file for cron logs
RUN mkdir -p /home/logs/; touch /home/logs/backup.log

# Create crontab entry for checking reminders
RUN echo "0 * * * * /usr/src/go/bin/go run /go/src/app/cron/cron.go >> /home/logs/backup.log 2>&1" >> /home/mycron
RUN crontab /home/mycron
RUN rm /home/mycron

EXPOSE 4000