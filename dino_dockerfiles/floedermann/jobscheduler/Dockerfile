FROM java:8-alpine

#SOS Jobscheduler download URL
ENV SOS_JS_URL https://download.sos-berlin.com/JobScheduler.1.12/jobscheduler_linux-x64.1.12.0.tar.gz
ENV SOS_JOC_URL https://download.sos-berlin.com/JobScheduler.1.12/joc_linux.1.12.0.tar.gz

#add packages - needed for alpine
RUN apk add --no-cache curl tar bash sed

#download and install scheduler
RUN curl -o /root/jobscheduler.tar.gz $SOS_JS_URL
RUN mkdir /root/install && tar xzvf /root/jobscheduler.tar.gz -C /root/install --strip-components=1
COPY scheduler_install.xml /root/install/scheduler_install.xml

#download joc cockpit
RUN curl -o /root/joc_cockpit.tar.gz $SOS_JOC_URL
RUN mkdir /root/install/joc && tar xzvf /root/joc_cockpit.tar.gz -C /root/install/joc --strip-components=1
COPY joc_install.xml /root/install/joc/joc_install.xml

#install
COPY startup_scheduler.sh /opt/startup_scheduler.sh

#expose scheduler ports
EXPOSE 40444 48444 4444 4446 40446

#start wrapper script
RUN chmod +x /opt/startup_scheduler.sh
CMD ["bash","/opt/startup_scheduler.sh"]
