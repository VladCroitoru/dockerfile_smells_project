FROM scratch

MAINTAINER renlar <renlar@liddev.com>

ADD https://github.com/redock/tiny-arch/releases/download/0.3.0/root.x86_64.tar.gz /root.x86_64.tar.gz
ADD util/utar /utar
RUN ["/utar", "root.x86_64.tar.gz"]

RUN pacman -Scc --noconfirm \
    && chmod 777 /tmp \
    #remove unecessary files
    #&& rm -rf /usr/share/doc /usr/share/man /usr/share/info /usr/share/locale /var/cache/pacman/pkg/* \
    #&& echo "unset HISTFILE" >> /etc/profile
