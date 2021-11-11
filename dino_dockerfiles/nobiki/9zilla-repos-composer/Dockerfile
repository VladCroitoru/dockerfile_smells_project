FROM debian:stretch
MAINTAINER Naoaki Obiki
RUN apt-get update && apt-get install -y sudo git supervisor systemd
ARG username="git"
RUN groupadd $username && useradd -g $username -d /home/$username $username && mkdir /home/$username
RUN apt-get update && apt-get install -y git-core
ADD settings/git-daemon/.gitconfig /home/$username
ADD settings/supervisor/conf.d/git-daemon.conf /git-daemon.conf.org
RUN chown -R $username:$username /home/$username
RUN echo "mkdir -p /repos/git && chown -R $username:$username /repos/git/" >> /git-daemon.sh && chmod +x /git-daemon.sh
RUN apt-get install -y php php-all-dev php-cgi php-cli php-curl php-mbstring mcrypt imagemagick
RUN curl -sS "https://getcomposer.org/installer" | php -- --install-dir=/usr/local/bin
RUN mkdir -p /home/$username/.composer && chown -R $username:$username /home/$username/.composer
ENV COMPOSER_HOME /home/$username/.composer
RUN mkdir /usr/local/lib/satis/ && chown $username:$username /usr/local/lib/satis/
RUN sudo -u $username composer.phar create-project composer/satis:dev-master --keep-vcs --working-dir=/usr/local/lib/
ADD settings/satis/satis.json.org /usr/local/lib/satis/
RUN chown -R $username:$username /usr/local/lib/satis/
RUN ln -s /usr/local/lib/satis/bin/satis /usr/local/bin/satis
RUN apt-get install -y nginx && chmod 755 /var/log/nginx/
ADD settings/nginx/nginx.conf /etc/nginx/
ADD settings/supervisor/conf.d/nginx.conf /etc/supervisor/conf.d/
COPY bootstrap.sh /
RUN chmod +x /bootstrap.sh
CMD ["/bootstrap.sh"]
