# Version: 0.0.1
FROM base/archlinux:latest

MAINTAINER Phong V. Cao "phongvcao@phongvcao.com"

ENV REFRESH_AT "2015-06-06 10:56 PM"
ENV HOME "/home/phongvcao"
ENV anhVietDir "/usr/share/stardict/dic/AnhViet"
ENV vietAnhDir "/usr/share/stardict/dic/VietAnh"
ENV LANG C.UTF-8

RUN useradd --create-home phongvcao
RUN echo -e "phongvcao\nphongvcao" | passwd phongvcao
RUN echo -e "phongvcao\nphongvcao" | passwd root
RUN usermod phongvcao -G wheel

COPY mirrorlist /etc/pacman.d/mirrorlist
COPY mirrorlist.pacnew /etc/pacman.d/mirrorlist.pacnew

RUN rm -rf /etc/pacman.d/gnupg
RUN pacman-key --init
RUN pacman-key --populate archlinux
RUN pacman-key --refresh-keys
RUN pacman-db-upgrade
RUN pacman --noconfirm -Syyu
RUN pacman-db-upgrade
RUN pacman --noconfirm -S python python2 python-pip python2-pip vim-python3 \
        git sudo ranger ruby unzip sdcv vimpager openssh htop man

RUN systemctl enable sshd

RUN sed -r -i 's/\# %(wheel|sudo)/%\1/' /etc/sudoers
RUN sed -i \-e 's/^#*\(PermitRootLogin\) .*/\1 yes/' \
        -e 's/^#*\(PasswordAuthentication\) .*/\1 yes/' \
        -e 's/^#*\(PermitEmptyPasswords\) .*/\1 yes/' \
        -e 's/^#*\(UsePAM\) .*/\1 no/' \
        -e 's/^#*\(Port\) .*/\1 22/' \
        /etc/ssh/sshd_config

RUN /usr/bin/ssh-keygen -A

USER phongvcao

RUN git clone https://github.com/phongvcao/dotfiles.git /home/phongvcao/.dotfiles
RUN mkdir /home/phongvcao/.config
RUN for f in $(command ls -A /home/phongvcao/.dotfiles/config); do ln -s -f /home/phongvcao/.dotfiles/config/$f /home/phongvcao/.config/$f; done
RUN for f in $(command ls -A /home/phongvcao/.dotfiles/rcs); do ln -s -f /home/phongvcao/.dotfiles/rcs/$f /home/phongvcao/.$f; done

RUN echo -e "phongvcao" | sudo mkdir -p /usr/share/stardict/dic/
RUN unzip "${HOME}/.dotfiles/root${anhVietDir}.zip" -d "${HOME}/.dotfiles/root${anhVietDir}"
RUN unzip "${HOME}/.dotfiles/root${vietAnhDir}.zip" -d "${HOME}/.dotfiles/root${vietAnhDir}"
RUN echo -e "phongvcao" | sudo mv "${HOME}/.dotfiles/root${anhVietDir}" "${anhVietDir}"
RUN echo -e "phongvcao" | sudo mv "${HOME}/.dotfiles/root${vietAnhDir}" "${vietAnhDir}"

RUN mkdir -p /home/phongvcao/.gem/ruby/2.2.0/bin/
RUN gem install mdl

EXPOSE 22

ENV USER "phongvcao"

CMD ["/bin/bash", "-c", "echo -e phongvcao | sudo /usr/bin/sshd -D"]
