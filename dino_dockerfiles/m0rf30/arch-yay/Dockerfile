FROM archlinux/base:latest
LABEL authors="M0Rf30"
RUN pacman -Syyu --noconfirm --noprogressbar && \
    pacman -S --noconfirm --needed --noprogressbar \
    base-devel \
    git \
&& groupadd --system sudo \
&& useradd -m --groups sudo user \
&& sed -i -e "s/Defaults    requiretty.*/ #Defaults    requiretty/g" /etc/sudoers \
&& echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
&& su - user -c "cd /home/user \
&& git clone https://aur.archlinux.org/yay-bin.git" \
&& su - user -c "cd /home/user/yay-bin && makepkg -s" \
&& cd /home/user/yay-bin && pacman -U yay-*.tar.zst --noconfirm \
&& rm -rf /home/user/yay-bin \
&& echo "LC_ALL=en_US.UTF-8" >> /etc/environment \
&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
&& echo "LANG=en_US.UTF-8" > /etc/locale.conf \
&& rm -rf /var/cache/pacman/pkg/* \
&& rm -rf /home/user/.cache \
&& locale-gen en_US.UTF-8
ENV LC_CTYPE 'en_US.UTF-8'

USER user
