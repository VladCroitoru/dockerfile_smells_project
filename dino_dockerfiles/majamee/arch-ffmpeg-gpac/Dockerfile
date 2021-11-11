FROM                archlinux:base

COPY                ./transcode.sh /bin/transcode.sh

                    # WORKAROUND for glibc 2.33 and old Docker
                    # See https://github.com/actions/virtual-environments/issues/2658
                    # Thanks to https://github.com/lxqt/lxqt-panel/pull/1562
RUN                 patched_glibc=glibc-linux4-2.33-4-x86_64.pkg.tar.zst && \
                    curl -LO "https://repo.archlinuxcn.org/x86_64/$patched_glibc" && \
                    bsdtar -C / -xvf "$patched_glibc"
                    
                    
RUN                 pacman -Sy --noconfirm && \
                    pacman -S --noconfirm ffmpeg gpac git libxslt && \
                    pacman -Scc --noconfirm && \
                    git clone https://github.com/squidpickles/mpd-to-m3u8.git /app/mpd-to-m3u8 && \
                    chmod +x /bin/transcode.sh

COPY                ./src /app/src

WORKDIR             /video
ENTRYPOINT          ["/bin/transcode.sh"]
CMD                 ["*.mkv"]
