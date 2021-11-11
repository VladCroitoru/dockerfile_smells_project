FROM crux
MAINTAINER Shin Sterneck <shin at sterneck dot asia>

RUN	mkdir /usr/ports/{work,pkgs,src} 
RUN	sed -i 's|\(prtdir /usr/ports/xorg\)|\1\nprtdir /usr/ports/contrib|' /etc/prt-get.conf

RUN	sed -i 's|#\ \(PKGMK_WORK_DIR=\)\(.*\)|#\1\2\n\1"/usr/ports/work/${PWD##*/}"|' /etc/pkgmk.conf && \
        sed -i 's|#\ \(PKGMK_PACKAGE_DIR=\)\(.*\)|#\1\2\n\1"/usr/ports/pkgs"|' /etc/pkgmk.conf && \
        sed -i 's|#\ \(PKGMK_SOURCE_DIR=\)\(.*\)|#\1\2\n\1"/usr/ports/src"|' /etc/pkgmk.conf && \
        sed -i 's|#\ \(.*MAKEFLAGS=\)\(.*\)|#\1\2\n\1"-j$(expr $(nproc) + 1)"|' /etc/pkgmk.conf && \
	sed -i 's|#\ \(PKGMK_IGNORE_FOOTPRINT=\)\(.*\)|#\1\2\n\1"yes"|' /etc/pkgmk.conf 

RUN	mv /etc/ports/contrib.rsync.inactive /etc/ports/contrib.rsync

RUN	ports -u

RUN	prt-get sysup && \
	rm -rf /usr/ports/{work,pkgs,src}/*

