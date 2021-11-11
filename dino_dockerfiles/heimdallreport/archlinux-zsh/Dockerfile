FROM heimdallreport/archlinux-minimal

RUN pacman --noconfirm  -S grep \
	#&& pacman -Sg base | grep -v -e cryptsetup \
	#-e device-mapper \
	#-e dhcpcd \
	#-e iproute2 \
	#-e jfsutils \
	#-e linux \
	#-e lvm2 \
	#-e man-db \
	#-e man-pages \
	#-e mdadm \
	#-e nano \
	#-e netctl \
	#-e openresolv \
	#-e pciutils \
	#-e pcmciautils \
	#-e reiserfsprogs \
	#-e s-nail \
	#-e systemd-sysvcompat \
	#-e usbutils \
	#-e vi \
	#-e xfsprogs \
	#| sed "s/^base //g" | pacman --noconfirm  -S -	\
	&& pacman --noconfirm -S grml-zsh-config zsh zsh-completions zsh-lovers vim net-tools \
	#&& paccache -r -k0 \
	&& pacman -Scc --noconfirm \
	&& echo >> /etc/skel/.vimrc \
	&& cp /etc/skel/.vimrc /etc/skel/.zshrc /root/ \
	&& chsh -s /bin/zsh \
	&& useradd -D -s /bin/zsh
