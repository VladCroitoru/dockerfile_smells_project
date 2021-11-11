FROM base/archlinux:latest
LABEL maintainer="Nicolas Surleraux <nsurleraux@gmail.com>"

RUN pacman -Syy --noconfirm 
RUN pacman -S libglvnd virtualbox-host-modules-arch virtualbox vagrant git --noconfirm 
RUN rm -rf /var/lib/pacman/sync/*

COPY gitvagrant.sh ./gitvagrant.sh
RUN chmod +x ./gitvagrant.sh

ENTRYPOINT ["./gitvagrant.sh"]
