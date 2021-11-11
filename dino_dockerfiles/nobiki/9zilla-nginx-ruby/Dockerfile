FROM debian:stretch
MAINTAINER Naoaki Obiki
RUN apt-get update && apt-get install -y sudo git systemd
ARG username="9zilla"
ARG password="9zilla"
RUN mkdir /home/$username && useradd -s /bin/bash -d /home/$username $username && echo "$username:$password" | chpasswd && echo ${username}' ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/$username && mkdir -p /home/$username/ci && chown -R $username:$username /home/$username
RUN apt-get install -y make autoconf automake gcc g++ vim tig dbus bash-completion supervisor bzip2 unzip pigz p7zip-full tree sed locales dialog chrony openssl curl wget aria2 ftp ncftp subversion expect cron dnsutils procps siege htop inetutils-traceroute iftop screen byobu lsb-release
RUN locale-gen ja_JP.UTF-8 && localedef -f UTF-8 -i ja_JP ja_JP
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:jp
ENV LC_ALL ja_JP.UTF-8
RUN cp -p /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && sed -ri "s/^server 0.debian.pool.ntp.org/#server 0.debian.pool.ntp.org/" /etc/chrony/chrony.conf && sed -ri "s/^server 1.debian.pool.ntp.org/#server 1.debian.pool.ntp.org/" /etc/chrony/chrony.conf && sed -ri "s/^server 2.debian.pool.ntp.org/#server 2.debian.pool.ntp.org/" /etc/chrony/chrony.conf && sed -ri "s/^server 3.debian.pool.ntp.org/#server 3.debian.pool.ntp.org/" /etc/chrony/chrony.conf && echo "server ntp0.jst.mfeed.ad.jp" >> /etc/chrony/chrony.conf && echo "server ntp1.jst.mfeed.ad.jp" >> /etc/chrony/chrony.conf && echo "server ntp2.jst.mfeed.ad.jp" >> /etc/chrony/chrony.conf && echo "allow 172.18/12" >> /etc/chrony/chrony.conf && systemctl enable chrony
RUN mkdir -p /usr/local/src/dotfiles/ && git clone "https://nobiki@bitbucket.org/nobiki/dotfiles.git" /usr/local/src/dotfiles/ && cp /etc/bash.bashrc /home/$username/.bashrc && chown $username:$username /home/$username/.bashrc && cp /usr/local/src/dotfiles/.bash_profile /home/$username/.bash_profile && chown $username:$username /home/$username/.bash_profile && cp /usr/local/src/dotfiles/.gitconfig /home/$username/.gitconfig && chown $username:$username /home/$username/.gitconfig && cp /usr/local/src/dotfiles/.screenrc /home/$username/.screenrc && chown $username:$username /home/$username/.screenrc && mkdir -p /home/$username/.ssh/ && cp /usr/local/src/dotfiles/.ssh/config /home/$username/.ssh/config && chown -R $username:$username /home/$username/.ssh/ && echo "export LANG=ja_JP.UTF-8" >> /home/$username/.bash_profile && echo "export LANGUAGE=ja_JP:jp" >> /home/$username/.bash_profile && echo "export LC_ALL=ja_JP.UTF-8" >> /home/$username/.bash_profile
RUN curl -o /usr/local/bin/jq "http://stedolan.github.io/jq/download/linux64/jq" && chmod +x /usr/local/bin/jq
RUN echo 'if [ -e $HOME/.anyenv/bin ]; then' >> /home/$username/.bash_profile && echo '  export PATH="$HOME/.anyenv/bin:$PATH"' >> /home/$username/.bash_profile && echo '  eval "$(anyenv init -)"' >> /home/$username/.bash_profile && echo 'fi' >> /home/$username/.bash_profile
RUN wget "https://dl.eff.org/certbot-auto" -P /usr/local/bin/ && chmod a+x /usr/local/bin/certbot-auto && /usr/local/bin/certbot-auto --os-packages-only --non-interactive
RUN apt-get install -y direnv && echo 'eval "$(direnv hook bash)"' >> /home/$username/.bash_profile
RUN apt-get install -y libssl-dev libreadline-dev zlib1g-dev
RUN apt-get install -y nginx && chmod 755 /var/log/nginx/
ADD settings/nginx/nginx.conf /etc/nginx/
ADD settings/supervisor/conf.d/nginx.conf /etc/supervisor/conf.d/
RUN apt-get install -y mariadb-client default-libmysqlclient-dev
COPY bootstrap.sh /
RUN chmod +x /bootstrap.sh
CMD ["/bootstrap.sh"]
