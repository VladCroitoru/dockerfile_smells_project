FROM archlinux/archlinux:base
MAINTAINER vladus2000 <docker@matt.land>

COPY shiz/ /

RUN \
	pacman -Syyu --noconfirm --needed audit && \
	echo alias 'cd..="cd .."' >> /etc/bash.bashrc && \
	echo alias 'l="ls -CF"' >> /etc/bash.bashrc && \
	echo alias 'la="ls -A"' >> /etc/bash.bashrc && \
	echo alias 'll="ls -alF"' >> /etc/bash.bashrc && \
	echo alias 'lld="ls -ald"' >> /etc/bash.bashrc && \
	echo alias 'lrt="ls -lrt"' >> /etc/bash.bashrc && \
	echo alias 'lrta="ls -lrta"' >> /etc/bash.bashrc && \
	echo alias 'netstat="ss"' >> /etc/bash.bashrc && \
	echo alias 'p="pgrep -af "' >> /etc/bash.bashrc && \
	chmod +x /*.sh && \
	rm -rf /usr/share/man/* /README /etc/pacman.d/mirrorlist.pacnew && \
	rm -rf /var/cache/pacman/pkg/* /var/lib/pacman/sync/*

CMD /bin/bash -c /startup.sh

