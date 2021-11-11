FROM docker.pkg.github.com/dock0/amylum_arch/amylum_arch:20200214-243cea1
MAINTAINER akerl <me@lesaker.org>
RUN yes | pacman -Syu --force --needed --nodeps \
    curl-amylum \
    gmp-amylum \
    gnupg-amylum \
    gpgme-amylum \
    krb5-amylum \
    libarchive-amylum \
    libassuan-amylum \
    libgcrypt-amylum \
    libgpg-error-amylum \
    libtasn1-amylum \
    libunistring-amylum \
    musl-amylum \
    nettle-amylum \
    openssh-amylum \
    openssl-amylum \
    p11-kit-amylum \
    pacman-amylum \
    pacman-mirrorlist-amylum \
    sqlite-amylum
RUN mv /etc/pacman.conf.pacsave /etc/pacman.conf && \
    mv /etc/pacman.d/mirrorlist.pacsave /etc/pacman.d/mirrorlist
RUN cp /usr/bin/xz /usr/local/bin/ && \
    cp -a /usr/lib/liblzma* /usr/local/lib && \
    echo "/usr/local/lib" > /etc/ld.so.conf.d/local.conf && \
    ldconfig && \
    yes | pacman -S xz-amylum && \
    rm -f /usr/local/bin/xz /usr/local/lib/liblzma* /etc/ld.so.conf.d/local.conf && \
    ldconfig
RUN yes | pacman -S --needed \
    bash-amylum \
    coreutils-amylum \
    git-amylum \
    gzip-amylum \
    iproute2-amylum \
    iputils-amylum \
    procps-ng-amylum \
    shadow-amylum \
    tar-amylum \
    util-linux-amylum \
    which-amylum \
    zlib-amylum
RUN pacman -R --noconfirm \
    libldap \
    e2fsprogs
