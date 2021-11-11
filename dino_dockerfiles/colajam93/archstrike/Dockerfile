FROM colajam93/archlinux:latest
MAINTAINER colajam93 <https://github.com/colajam93>

USER root
RUN echo -e "[multilib]\n"\
            "Include = /etc/pacman.d/mirrorlist\n"\
            "[archstrike]\n"\
            "Server = https://mirror.archstrike.org/\$arch/\$repo\n"\
            "[archstrike-testing]\n"\
            "Server = https://mirror.archstrike.org/\$arch/\$repo" >> /etc/pacman.conf && \
    pacman-key --init &> /dev/null  && \
    dirmngr < /dev/null &> /dev/null && \
    pacman-key -r 9D5F1C051D146843CDA4858BDE64825E7CBC0D51 &> /dev/null && \
    pacman-key --lsign-key 9D5F1C051D146843CDA4858BDE64825E7CBC0D51 &> /dev/null && \
    pacman --noconfirm -Syu archstrike-keyring archstrike-mirrorlist &> /dev/null && \
    sed -i 's/Server = https:\/\/mirror.archstrike.org\/\$arch\/\$repo/Include = \/etc\/pacman.d\/archstrike-mirrorlist/' /etc/pacman.conf
USER test
