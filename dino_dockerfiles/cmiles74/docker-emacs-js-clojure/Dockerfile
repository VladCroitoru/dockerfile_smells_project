from dock0/arch:latest

# update our Arch installation
# run pacman-key --init
# run pacman-key --populate archlinux
# run pacman-key --refresh-keys
# run pacman -Syu --noconfirm
# run pacman-db-upgrade

# install requirements
run pacman -Syqu --noconfirm base-devel binutils tmux bash man fish powerline git openssh wget curl rxvt-unicode xorg-xrdb aspell-en gtk2 lib32-glibc bdf-unifont

# install httpie
run pacman -Syqu --noconfirm httpie

# install node and npm
run pacman -Syqu --noconfirm nodejs npm

# setup our developer user
workdir /root
run groupadd -r developer -g 1000
run useradd -u 1000 -r -g developer -d /developer -c "Software Developer" developer
copy /developer /developer
run chown -R developer:developer /developer
run chmod +x /developer/bin/*
run echo "%developer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# install leiningen
run curl -O https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
run chmod +x lein
run mv lein /sbin

# install Emacs
run pacman -Sqyu --noconfirm xorg-fonts-encodings xorg-font-utils git emacs

# install Java
run pacman -Sy --noconfirm jdk8-openjdk java-openjfx maven

# build launch4j package
user developer
workdir /developer
run mkdir aur
run git clone https://aur.archlinux.org/launch4j.git aur/launch4j
workdir /developer/aur/launch4j
run makepkg
user root
run pacman -U --noconfirm *xz

# build hack aur package
user developer
workdir /developer
run git clone https://aur.archlinux.org/ttf-hack.git aur/ttf-hack
workdir /developer/aur/ttf-hack
run makepkg
user root
run pacman -U --noconfirm *xz

# build nvm aur package
user developer
workdir /developer
run git clone https://aur.archlinux.org/nvm.git aur/nvm
workdir /developer/aur/nvm
run makepkg
user root
run pacman -U --noconfirm *xz

# build watchman aur package
user developer
workdir /developer
run git clone https://aur.archlinux.org/watchman.git aur/watchman
workdir /developer/aur/watchman
run makepkg
user root
run pacman -U --noconfirm *xz

# cleanup aur packages
user root
workdir /developer
run rm -rf aur

# install some NPM packages
user root
run npm install -g gulp tern js-beautify jshint eslint babel-eslint eslint-plugin-react

# install spacemacs
user developer
workdir /developer
run git clone --recursive https://github.com/syl20bnr/spacemacs ~/.emacs.d

# setup leiningen
run /sbin/lein --version

# volume used for mounting project files
copy project /project
workdir /project

#
# Environment Variables
#

# setup nvm
run source /usr/share/nvm/init-nvm.sh

# Path
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk
ENV PATH $JAVA_HOME/bin:$PATH

#
# Ports
#

# BrowserSync
expose 3000
expose 3001

# ember server
expose 49153
expose 4200

# Web application
expose 5000

#
# Volumes
#

# the project files
volume ["/project"]

# start emacs
user developer
entrypoint ["/developer/bin/start-emacs"]
