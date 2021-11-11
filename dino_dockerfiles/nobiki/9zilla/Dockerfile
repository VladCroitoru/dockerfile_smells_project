FROM debian:stretch
MAINTAINER Naoaki Obiki
RUN apt-get update && apt-get install -y sudo git
ARG username="9zilla"
ARG password="9zilla"
RUN mkdir /home/$username && useradd -s /bin/bash -d /home/$username $username && echo "$username:$password" | chpasswd && echo ${username}' ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/$username && mkdir -p /home/$username/ci && chown -R $username:$username /home/$username
RUN apt-get install -y ssh
RUN sed -ri "s/^UsePAM yes/#UsePAM yes/" /etc/ssh/sshd_config && sed -ri "s/^#UsePAM no/UsePAM no/" /etc/ssh/sshd_config && sed -ri "s/^#PasswordAuthentication yes/PasswordAuthentication yes/" /etc/ssh/sshd_config && mkdir -p /var/run/sshd
ADD settings/supervisor/conf.d/sshd.conf /etc/supervisor/conf.d/
RUN apt-get install -y make autoconf automake gcc g++ vim tig dbus bash-completion supervisor bzip2 unzip pigz p7zip-full tree sed locales dialog chrony openssl curl wget aria2 ftp ncftp subversion expect cron dnsutils procps siege htop inetutils-traceroute iftop screen byobu lsb-release
RUN locale-gen ja_JP.UTF-8 && localedef -f UTF-8 -i ja_JP ja_JP
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:jp
ENV LC_ALL ja_JP.UTF-8
RUN cp -p /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && sed -ri "s/^server 0.debian.pool.ntp.org/#server 0.debian.pool.ntp.org/" /etc/chrony/chrony.conf && sed -ri "s/^server 1.debian.pool.ntp.org/#server 1.debian.pool.ntp.org/" /etc/chrony/chrony.conf && sed -ri "s/^server 2.debian.pool.ntp.org/#server 2.debian.pool.ntp.org/" /etc/chrony/chrony.conf && sed -ri "s/^server 3.debian.pool.ntp.org/#server 3.debian.pool.ntp.org/" /etc/chrony/chrony.conf && echo "server ntp0.jst.mfeed.ad.jp" >> /etc/chrony/chrony.conf && echo "server ntp1.jst.mfeed.ad.jp" >> /etc/chrony/chrony.conf && echo "server ntp2.jst.mfeed.ad.jp" >> /etc/chrony/chrony.conf && echo "allow 172.18/12" >> /etc/chrony/chrony.conf && systemctl enable chrony
RUN mkdir -p /usr/local/src/dotfiles/ && git clone "https://nobiki@bitbucket.org/nobiki/dotfiles.git" /usr/local/src/dotfiles/ && cp /etc/bash.bashrc /home/$username/.bashrc && chown $username:$username /home/$username/.bashrc && cp /usr/local/src/dotfiles/.bash_profile /home/$username/.bash_profile && chown $username:$username /home/$username/.bash_profile && cp /usr/local/src/dotfiles/.gitconfig /home/$username/.gitconfig && chown $username:$username /home/$username/.gitconfig && cp /usr/local/src/dotfiles/.screenrc /home/$username/.screenrc && chown $username:$username /home/$username/.screenrc && mkdir -p /home/$username/.ssh/ && cp /usr/local/src/dotfiles/.ssh/config /home/$username/.ssh/config && chown -R $username:$username /home/$username/.ssh/ && echo "export LANG=ja_JP.UTF-8" >> /home/$username/.bash_profile && echo "export LANGUAGE=ja_JP:jp" >> /home/$username/.bash_profile && echo "export LC_ALL=ja_JP.UTF-8" >> /home/$username/.bash_profile
RUN curl -o /usr/local/bin/jq "http://stedolan.github.io/jq/download/linux64/jq" && chmod +x /usr/local/bin/jq
RUN echo 'if [ -e $HOME/.anyenv/bin ]; then' >> /home/$username/.bash_profile && echo '  export PATH="$HOME/.anyenv/bin:$PATH"' >> /home/$username/.bash_profile && echo '  eval "$(anyenv init -)"' >> /home/$username/.bash_profile && echo 'fi' >> /home/$username/.bash_profile
RUN apt-get install -y yui-compressor pandoc mutt msmtp bmon iptraf nload slurm sl toilet lolcat
RUN curl -o /usr/local/bin/hcat "https://raw.githubusercontent.com/nobiki/bash-hcat/master/hcat" && chmod +x /usr/local/bin/hcat
RUN git clone "https://github.com/tkengo/highway.git" /usr/local/lib/highway && /usr/local/lib/highway/tools/build.sh && ln -s /usr/local/lib/highway/hw /usr/local/bin/hw
RUN mkdir -p /usr/local/lib/sql-formatter/ && chown $username:$username /usr/local/lib/sql-formatter/ && git clone "https://github.com/jdorn/sql-formatter" /usr/local/lib/sql-formatter && ln -s /usr/local/lib/sql-formatter/bin/sql-formatter /usr/local/bin/sql-formatter
RUN apt-get install -y libncurses5 libncurses5-dev libncursesw5 libncursesw5-dev libreadline-dev pkg-config && git clone "https://github.com/dvorka/hstr.git" /usr/local/lib/hstr && cd /usr/local/lib/hstr/dist && ./1-dist.sh && cd /usr/local/lib/hstr && ./configure && make && make install
RUN curl "http://downloads.drone.io/release/linux/amd64/drone.tar.gz" | tar zx && install -t /usr/local/bin drone
ADD archives/peco_linux_amd64/peco /usr/local/bin/
RUN chmod +x /usr/local/bin/peco
ADD archives/memo_linux_amd64/memo /usr/local/bin/
RUN chmod +x /usr/local/bin/memo
RUN git clone "https://github.com/soimort/translate-shell" /usr/local/src/translate-shell && cd /usr/local/src/translate-shell && make && make install
RUN git clone "https://github.com/b4b4r07/enhancd.git" /usr/local/src/enhancd && chmod +x /usr/local/src/enhancd/init.sh && echo 'source /usr/local/src/enhancd/init.sh' >> /home/$username/.bash_profile
ADD archives/ngrok /usr/local/bin/
RUN chmod +x /usr/local/bin/ngrok
RUN wget "https://raw.githubusercontent.com/greymd/tmux-xpanes/master/bin/xpanes" -O /usr/local/bin/xpanes && chmod +x /usr/local/bin/xpanes
RUN wget "https://dl.eff.org/certbot-auto" -P /usr/local/bin/ && chmod a+x /usr/local/bin/certbot-auto && /usr/local/bin/certbot-auto --os-packages-only --non-interactive
RUN apt-get install -y direnv && echo 'eval "$(direnv hook bash)"' >> /home/$username/.bash_profile
RUN apt-get install -y nginx && chmod 755 /var/log/nginx/
ADD settings/nginx/nginx.conf /etc/nginx/
ADD settings/supervisor/conf.d/nginx.conf /etc/supervisor/conf.d/
RUN apt-get install -y mariadb-client default-libmysqlclient-dev
RUN apt-get install -y postgresql-client
RUN apt-get install -y php php-all-dev php-cgi php-cli php-curl php-mbstring mcrypt imagemagick
RUN apt-get install -y re2c bison pkg-config xz-utils libssl-dev libxml2-dev libcurl4-gnutls-dev libjpeg62-turbo-dev libpng-dev libicu-dev libmcrypt-dev libreadline-dev libtidy-dev libxslt1-dev imagemagick autoconf
COPY settings/php/default_configure_options /
RUN curl -sS "https://getcomposer.org/installer" | php -- --install-dir=/usr/local/bin
RUN mkdir -p /home/$username/.composer && chown -R $username:$username /home/$username/.composer
ENV COMPOSER_HOME /home/$username/.composer
RUN apt-get install -y vim-nox pkg-config make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libfreetype6-dev llvm libncurses5 libncurses5-dev libncursesw5 libncursesw5-dev xz-utils tk-dev
RUN apt-get install -y libssl-dev libreadline-dev zlib1g-dev
ENV DISPLAY :99
RUN apt-get install -y xvfb
RUN echo "Xvfb $DISPLAY -screen 0 1920x1200x24 > /dev/null &" > /usr/local/bin/selenium-xvfb && chmod +x /usr/local/bin/selenium-xvfb
COPY bootstrap.sh /
RUN chmod +x /bootstrap.sh
CMD ["/bootstrap.sh"]
