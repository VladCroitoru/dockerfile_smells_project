FROM webdevops/php-nginx:ubuntu-16.04

RUN apt update
RUN apt install -y openssh-server
RUN apt install -y vim git wget curl tmux fish tree jq
RUN git config --global user.email "admin@comicdatabase.com"
RUN git config --global user.name "Comic DataBase"
RUN apt install -y php-curl

ADD analyticstracking.php /app
ADD index.php /app
ADD save.php /app
ADD downtxlist.txt /app
ADD welcome.php /app
ADD crontabfile /app
ADD tx2bdrun /app
ADD tx2bd.fish /app
ADD favicon.ico /app
ADD logo.jpg /app
ADD run.fish /app

RUN git clone https://github.com/ComicDatabase/ComicDatabase.git
RUN mv ComicDatabase /app/comic
RUN echo 'root:root' | chpasswd
RUN chsh -s $(which fish)
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN crontab /app/crontabfile
RUN apt-get -y install rsyslog
RUN cp /app/crontabfile /etc/crontab
RUN touch /var/log/cron.log

EXPOSE 22 80 8000 8080

#CMD ["/usr/bin/fish","/app/run.fish"]
