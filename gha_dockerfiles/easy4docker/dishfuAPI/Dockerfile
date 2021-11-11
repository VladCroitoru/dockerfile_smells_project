FROM ubuntu
RUN apt update && apt autoremove
RUN apt -y install sudo curl dirmngr apt-transport-https lsb-release ca-certificates
RUN curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
RUN sudo apt -y install nodejs
RUN apt-get -y install git
RUN apt-get install -y cron
RUN apt-get -y install vim

RUN mkdir /var/_config

# RUN (crontab -l ; echo "@reboot sh /var/cronJobs/bootUp.sh >> /var/log/bootUp.log") | crontab
RUN (crontab -l ; echo "* * * * * sh /var/cronJobs/cronMin.sh >> /var/log/cronMin.log") | crontab
RUN (crontab -l ; echo "*/5 * * * * sh /var/cronJobs/cron5Mins.sh >> /var/log/cron5Mins.log") | crontab
RUN (crontab -l ; echo "*/15 * * * * sh /var/cronJobs/cron15Mins.sh >> /var/log/cron15Mins.log") | crontab
RUN (crontab -l ; echo "*/30 * * * * sh /var/cronJobs/cron30Mins.sh >> /var/log/cron30Mins.log") | crontab
RUN (crontab -l ; echo "3 * * * * sh /var/cronJobs/cron1hr.sh >> /var/log/cron1hr.log") | crontab

# CMD cron -f
CMD sh /var/cronJobs/bootUp.sh >> /var/log/bootUp.log
