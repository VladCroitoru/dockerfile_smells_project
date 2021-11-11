FROM base/archlinux

RUN curl -Lk 'https://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.7-201706120950/eclipse-SDK-4.7-linux-gtk-x86_64.tar.gz&r=1' | tar xvz

RUN pacman --noconfirm -Syu archlinux-keyring reflector rsync && \
    reflector --verbose -l 200 -f 50 --sort rate | tee /etc/pacman.d/mirrorlist && \
    pacman --noconfirm -S sed grep which diffutils gawk gettext gzip tar file git tigervnc gtk3 jdk8-openjdk nmap vi ttf-liberation && \
    pacman --noconfirm -Rnsu reflector rsync && \
    paccache -rk0
