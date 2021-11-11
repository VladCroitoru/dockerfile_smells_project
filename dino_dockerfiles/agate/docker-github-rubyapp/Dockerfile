FROM phusion/passenger-ruby23

RUN apt-get update && apt-get -y upgrade && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm -f /etc/service/nginx/down

ADD nginx-default-site /etc/nginx/sites-available/default
ADD ssh_config /root/.ssh/config
ADD pull_app.sh /etc/my_init.d/001_git_pull_app

EXPOSE 80
