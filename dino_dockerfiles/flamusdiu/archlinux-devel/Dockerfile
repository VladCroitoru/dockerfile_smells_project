FROM archlinux

RUN pacman -Syu --needed --noconfirm base-devel git fish openssh pacman-contrib
RUN useradd -ms /bin/fish arch \
	&& echo "arch ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \
	&& echo "set disable_coredump false" >> /etc/sudo.conf

USER arch
WORKDIR /home/arch

RUN git clone https://aur.archlinux.org/aura-bin.git  \
	&& cd aura-bin \
	&& makepkg -irs --noconfirm
