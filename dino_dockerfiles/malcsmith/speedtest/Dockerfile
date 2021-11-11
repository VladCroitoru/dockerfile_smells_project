FROM python:3.7-alpine
#MAINTAINER Malcolm Smith

# Install Supporting Packages
RUN apk --no-cache  -q update && \
  apk add --no-cache bash curl wget tini python3-dev gcc build-base
  #python3  wget py-pip tini pytest 
  #python-dev 
  #py-mysqldb  mysql-client 

ADD requirements.txt /
#  RUN pip install -U pip && pip install MySQL-python
 RUN  pip3 install -r requirements.txt

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/speedtest-cron
 
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/speedtest-cron
 
# Create the log file to be able to run tail
RUN touch /var/log/speedtest.log

#RUN crontab -l | { cat; echo "1,16,31,46 * * * *  /speedtest.py " ; echo "* * * * *           echo test" ; } | crontab -
 
# Grab the fresh version of speedtest
  RUN wget -O /speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
  RUN chmod a+x /speedtest-cli

  RUN wget -O  ookla-speedtest-1.0.0-x86_64-linux.tgz  https://bintray.com/ookla/download/download_file?file_path=ookla-speedtest-1.0.0-x86_64-linux.tgz
  RUN tar xvfz ookla-speedtest-1.0.0-x86_64-linux.tgz
  RUN /speedtest --accept-license --accept-gdpr

#copy and prep speedtest
  COPY speedtest_influx.py /speedtest_influx.py
  COPY test.py /test.py
  RUN chmod a+x /speedtest_influx.py
  RUN chmod a+x /test.py
  



# Run the command on container startup
#CMD ["/usr/sbin/crond", "-f"]
CMD /bin/bash