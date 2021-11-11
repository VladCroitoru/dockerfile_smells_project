FROM base/archlinux

RUN pacman --noconfirm -Sy && \
        pacman --noconfirm -S unzip git vim jdk8-openjdk maven apache-ant nodejs-lts-carbon npm yarn docker docker-compose apache iproute2 net-tools && \
        (echo -e "y\ny\n" | pacman -Scc)

RUN npm install -g --unsafe-perm phantomjs webpack

# setup default locale = en_US.UTF-8
RUN sed -i '/#\(ru_RU.UTF\|en_US.UTF\)/s/^#//' /etc/locale.gen
RUN locale-gen
ENV LANG="en_US.UTF-8"
