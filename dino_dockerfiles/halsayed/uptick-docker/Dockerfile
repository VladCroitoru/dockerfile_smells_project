FROM centos:centos7


RUN yum -y install epel-release
RUN yum -y install nginx
RUN yum -y install git
RUN curl --silent --location https://rpm.nodesource.com/setup_9.x | bash -
RUN yum -y install nodejs
RUN yum -y install supervisor
RUN yum -y install nrpe nagios-plugins-users nagios-plugins-load nagios-plugins-swap nagios-plugins-disk nagios-plugins-procs


WORKDIR /usr/src/uptick
RUN mkdir -p /var/log/supervisor

COPY . .
#COPY supervisord.conf /etc/supervisord.conf
RUN chmod +x uptick.sh

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf

RUN npm install

EXPOSE 80
EXPOSE 3000

CMD ["./uptick.sh"]




