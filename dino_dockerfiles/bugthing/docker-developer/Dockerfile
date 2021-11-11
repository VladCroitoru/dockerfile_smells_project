FROM bugthing/docker-archlinux

# Setup locale. Install packages. Setup sudo. Generate ssh key. Set root password. Add developer user.
RUN \
    echo 'en_GB.UTF-8 UTF-8' > /etc/locale.gen && echo 'LANG="en_GB.UTF-8"' > /etc/locale.conf && locale-gen &&\
    cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup &&\
    sed -i 's/^#Server/Server/' /etc/pacman.d/mirrorlist.backup &&\
    rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup > /etc/pacman.d/mirrorlist &&\
    pacman --noconfirm -Sy archlinux-keyring &&\
    pacman-key --populate &&\
    pacman-key --refresh-keys &&\
    pacman --noconfirm -Syyuu &&\
    pacman-db-upgrade &&\
    (yes | pacman -Syyu) &&\
    pacman -S --noconfirm base-devel libyaml postgresql-libs libmariadbclient \
      pkgfile ctags s3cmd ack wget curl ack supervisor cronie rsync aspell \
      openssh subversion git vim tmux ripgrep \
      jre8-openjdk sqlite python perl gconf imagemagick \
      xorg-server xorg-server-xvfb openbox x11vnc xterm phantomjs \
      docker syncthing firefox chromium pass \
      &&\
    \
    ssh-keygen -A &&\
    echo 'root:root' | chpasswd &&\
    echo "%wheel        ALL=NOPASSWD: ALL" >> /etc/sudoers &&\
    \
    useradd -m -g users -G wheel -s /bin/bash --home-dir /home/developer developer &&\
    echo 'developer:developer' | chpasswd

# chruby
ENV CHRUBY_VERSION 0.3.9
RUN wget -O chruby-$CHRUBY_VERSION.tar.gz https://github.com/postmodern/chruby/archive/v$CHRUBY_VERSION.tar.gz && tar -xzvf chruby-$CHRUBY_VERSION.tar.gz
RUN cd chruby-$CHRUBY_VERSION/ &&\
    make install &&\
    cd / &&\
    echo '[ -n "$BASH_VERSION" ] || [ -n "$ZSH_VERSION" ] || return' >> /etc/profile.d/chruby.sh &&\
    echo 'source /usr/local/share/chruby/chruby.sh' >> /etc/profile.d/chruby.sh &&\
    chmod +x /etc/profile.d/chruby.sh

# ruby-install (ruby installer)
ENV RUBYINSTALL_VERSION 0.6.1
RUN wget -O ruby-install-$RUBYINSTALL_VERSION.tar.gz https://github.com/postmodern/ruby-install/archive/v$RUBYINSTALL_VERSION.tar.gz &&\
    tar -xzvf ruby-install-$RUBYINSTALL_VERSION.tar.gz &&\
    rm ruby-install-$RUBYINSTALL_VERSION.tar.gz &&\
    cd ruby-install-$RUBYINSTALL_VERSION/ &&\
    make install &&\
    cd /

# nvm (nodejs installer and switcher)
ENV NVM_VERSION 0.32.1
RUN wget -O nvm-$NVM_VERSION.tar.gz https://github.com/creationix/nvm/archive/v$NVM_VERSION.tar.gz &&\
    tar -xzvf nvm-$NVM_VERSION.tar.gz &&\
    rm nvm-$NVM_VERSION.tar.gz &&\
    cp -a ./nvm-$NVM_VERSION /opt/nvm

# Add some configs
ADD files/sshd_config /etc/ssh/sshd_config

# Add service configs
ADD files/cron-supervisor.ini /etc/supervisor.d/cron.ini
ADD files/ssh-supervisor.ini /etc/supervisor.d/ssh.ini
ADD files/xvfb-supervisor.ini /etc/supervisor.d/xvfb.ini
ADD files/x11vnc-supervisor.ini /etc/supervisor.d/x11vnc.ini
ADD files/openbox-supervisor.ini /etc/supervisor.d/openbox.ini

# Expose port for ssh, web, vnc and some spares
EXPOSE 22 80 443 5900 8080 8081 8082 8083 8084 8085 8086 8087 8088 8089

# Become developer user from here
USER developer
WORKDIR /home/developer

# From AUR - Install pacaur
RUN \
    mkdir -p /home/developer/src &&\
    cd /home/developer/src &&\
    wget -O cower.tar.gz https://aur.archlinux.org/cgit/aur.git/snapshot/cower.tar.gz &&\
    tar xzf cower.tar.gz &&\
    cd cower &&\
    makepkg --noconfirm --skippgpcheck -s &&\
    sudo pacman -U --noconfirm cower-*.pkg.tar.xz &&\
    \
    cd /home/developer/src &&\
    wget -O pacaur.tar.gz https://aur.archlinux.org/cgit/aur.git/snapshot/pacaur.tar.gz &&\
    tar xzf pacaur.tar.gz &&\
    cd pacaur &&\
    makepkg --noconfirm --skippgpcheck -s &&\
    sudo pacman -U --noconfirm pacaur-*.pkg.tar.xz &&\
    \
    cd /

# Run the prepare script and fire up supervisord
CMD sudo /usr/bin/supervisord -n -c /etc/supervisord.conf
