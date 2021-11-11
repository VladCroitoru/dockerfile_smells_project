FROM nfnty/arch-mini
MAINTAINER AlbinoShaun "albinoshaun@hotmail.com"

RUN pacman -Syu --noconfirm && \
	pacman -S --noconfirm x2goserver mate mate-terminal sudo diffutils

RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key && \
	ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key && \
	ssh-keygen -b 521 -t ecdsa -C"$(id -un)@$(hostname)-$(date --rfc-3339=date)" -f /etc/ssh/ssh_host_ecdsa_key
	
RUN sed -i 's/^#X11Forwarding.*/X11Forwarding yes/' /etc/ssh/sshd_config && \
	sed -i 's/^# %wheel ALL=(ALL) ALL/%wheel ALL=(ALL) ALL/' /etc/sudoers && \
	useradd -m -G wheel shaun && \
	echo "shaun:arch2go" | chpasswd && \
	x2godbadmin --createdb

EXPOSE 22
CMD ["/usr/bin/sshd", "-D"]