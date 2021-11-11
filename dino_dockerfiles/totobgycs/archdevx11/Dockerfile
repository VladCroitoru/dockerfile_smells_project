FROM totobgycs/archdev
MAINTAINER totobgycs

ENV TERM xterm
RUN yaourt -Syy ; \
   yaourt -S --noconfirm xorg-server-common xorg-xhost xorg-xauth\
       ttf-ubuntu-font-family ttf-freefont freetype2 \
       mesa-libgl ; \
   yes | yaourt -Scc

RUN useradd -m guiuser ; \
   echo 'guiuser ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers 



