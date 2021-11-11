FROM frolvlad/alpine-python3

MAINTAINER Rune Langseid <runelangseid@gmail.com>

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN pip install -r requirements.txt

# Add crontab file in the cron directory
RUN echo '*/10 * * * * cd /src && python3 ./domeneshop.py >> /var/log/cron.log 2>&1' >> /etc/crontabs/root

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD crond && tail -f /var/log/cron.log
