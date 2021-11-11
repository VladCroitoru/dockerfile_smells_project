FROM archlinux
MAINTAINER Karl Hepworth <karl.hepworth@gmail.com>

RUN pacman -Syyu --noconfirm
RUN pacman -S --noconfirm ansible base-devel

RUN mkdir -p /.ansible/tmp && chmod -R 777 /.ansible

RUN mkdir -p /etc/ansible
RUN echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts

RUN ansible --version

USER 1000
CMD ["/usr/bin/bash"]
