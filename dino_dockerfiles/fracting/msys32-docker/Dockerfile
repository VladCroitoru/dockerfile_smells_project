FROM teaci/wine-staging
MAINTAINER Qian Hong <qhong@codeweavers.com>
# Work around https://bugs.wine-staging.com/show_bug.cgi?id=626
ENV WINPTY_SHOW_CONSOLE 1
COPY msys32-env /etc/
COPY msys64-env /etc/
COPY msys2-shell /usr/bin/
COPY msys2-rebase /usr/bin/
COPY msys32-init /usr/bin/
COPY msys32 /usr/bin/
COPY msys64 /usr/bin/
COPY mingw32 /usr/bin/
COPY mingw64 /usr/bin/
RUN msys32-init
RUN msys32 -c pacman -Sy --noconfirm --noprogressbar pacman mintty isl
RUN msys32 -c "pacman -Suu --needed --noconfirm --noprogressbar"
RUN msys32 -c "pacman -Suu --needed --noconfirm --noprogressbar && pacman -Scc --noconfirm"
RUN msys32 -c "pacman -S --needed --noconfirm --noprogressbar base-devel &&  pacman -Scc --noconfirm"
RUN msys32 -c "pacman -S --needed --noconfirm --noprogressbar msys2-devel && pacman -Scc --noconfirm"
RUN msys32 -c "pacman -S --needed --noconfirm --noprogressbar mingw-w64-i686-toolchain && pacman -Scc --noconfirm"
RUN msys32 -c "pacman -S --needed --noconfirm --noprogressbar git subversion && pacman -Scc --noconfirm"
RUN msys32 -c cp -f /usr/bin/false /usr/bin/tput
RUN msys2-rebase
