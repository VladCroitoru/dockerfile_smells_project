FROM base/devel


MAINTAINER Sebastiaan Koppe <mail@skoppe.eu>

RUN pacman -Sy --noconfirm git gcc make dub ldc libevent && \
        git clone https://github.com/skoppe/afl && \
        cd afl && \
        make && \
        pacman -Rns --noconfirm git make && \
    find /. -name "*~" -type f -delete && \
    bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \
    paccache -rk0 >/dev/null 2>&1 &&  \
    pacman-optimize && \
    rm -r /var/lib/pacman/sync/*
