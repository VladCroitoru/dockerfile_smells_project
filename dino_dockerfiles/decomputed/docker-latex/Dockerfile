FROM decomputed/docker-latex:no-fonts
LABEL maintainer="luis@decomputed.com"

## Update pacman
RUN pacman -Syyu --noconfirm

## Install tex-related thing
RUN pacman -S --noconfirm --noprogressbar --needed texlive-fontsextra

## Workdir will be `sources`
WORKDIR /sources