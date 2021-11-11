FROM l3iggs/archlinux
MAINTAINER Christian Ertler

# upgrade system and install dependencies
RUN pacman --noconfirm -Syyu && \
    pacman --noconfirm -S base-devel yajl sudo rsync

# add yaourt user and group
RUN groupadd -r yaourt && \
    useradd -r -g yaourt yaourt
RUN mkdir /tmp/yaourt && \
    chown -R yaourt:yaourt /tmp/yaourt

# configure sudo for pacman
ADD container_files/yaourt_sudo /etc/sudoers.d/yaourt

# install package-query
USER yaourt
RUN cd /tmp/yaourt && \
    curl https://aur.archlinux.org/packages/pa/package-query/package-query.tar.gz | tar zx && \
    cd /tmp/yaourt/package-query && \
    makepkg --noconfirm
USER root
RUN cd /tmp/yaourt/package-query && \
    pacman --noconfirm -U *.tar.xz

# install yaourt
USER yaourt
RUN cd /tmp/yaourt && \
    curl https://aur.archlinux.org/packages/ya/yaourt/yaourt.tar.gz | tar zx && \
	cd /tmp/yaourt/yaourt && \
	makepkg --noconfirm
USER root
RUN cd /tmp/yaourt/yaourt && \
	pacman --noconfirm -U *.tar.xz
