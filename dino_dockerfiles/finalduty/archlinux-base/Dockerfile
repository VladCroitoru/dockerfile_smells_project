FROM finalduty/archlinux
MAINTAINER FinalDuty <root@finalduty.me>
CMD /bin/bash

ADD https://raw.githubusercontent.com/finalduty/configs/master/.vimrc /root/
ADD https://raw.githubusercontent.com/finalduty/configs/master/.bashrc /root/

RUN pacman -Sy --noconfirm bash-completion vim lsof tcpdump; pacman -Scc --noconfirm &>/dev/null
