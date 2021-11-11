FROM archlinux/archlinux:base-devel

ARG MIRROR_QUERY_URL="https://www.archlinux.org/mirrorlist/?country=NL&country=DE&protocol=https&use_mirror_status=on"

LABEL maintainer="UPF"

ARG REPO_URL="https://upf.archlinux.be"

ENV PACKAGER="UPF Docker Container <vic@demuzere.be>" \
	USER_ID="1000" \
	GROUP_ID="1000" \
	PKG_HOME="/home/packager" \
	KEY_SERV="hkps://keys.openpgp.org"

# Init the package db & trust gpg keys
RUN \
	pacman-key --init && \
	pacman-key --populate archlinux && \
	pacman-key --keyserver "${KEY_SERV}" -r 560D6ECFDAC7134E51B1A127161C09A6CF1F8674 && \
	pacman-key --lsign CF1F8674 && \
	echo -e "\n[multilib]\nInclude = /etc/pacman.d/mirrorlist\n\n[upf]\nSigLevel = PackageRequired\nServer = ${REPO_URL}/\$arch\n\n[upf-any]\nSigLevel = PackageRequired\nServer=${REPO_URL}/any" >> /etc/pacman.conf && \
	pacman -Sy --noconfirm upf-keyring && \
	rm -f /var/cache/pacman/pkg/* /var/lib/pacman/sync/*

# Install all available updates & base-devel package group
RUN \
	curl -Ls "${MIRROR_QUERY_URL}" | sed -e 's/^#Server/Server/' -e '/^#/d' > /etc/pacman.d/mirrorlist && \
	pacman --noconfirm -Syu --needed base-devel && \
	rm -f /var/cache/pacman/pkg/* /var/lib/pacman/sync/*

# Configure packaging environment
RUN \
	groupadd -g "${GROUP_ID}" packager && \
	useradd -u "${USER_ID}" -g "${GROUP_ID}" -m packager && \
	echo "packager ALL=(ALL) NOPASSWD: /usr/bin/pacman" > /etc/sudoers.d/packager && \
	sed -i "s/#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/" /etc/locale.gen && \
	locale-gen && \
	echo "LANG=en_US.UTF-8" > /etc/locale.conf && \
	echo "LC_COLLATE=C" >> /etc/locale.conf

WORKDIR $PKG_HOME

COPY package.sh /opt

CMD [ "/bin/sh", "-c", "/opt/package.sh" ]
