FROM alanmquach/devcon-core:latest

MAINTAINER Alan Quach <integsrtite@gmail.com>

# i3 (236 MB)
ADD keyring.deb /root/keyring.deb
RUN apt install /root/keyring.deb \
    && echo "deb http://debian.sur5r.net/i3/ $(grep '^DISTRIB_CODENAME=' /etc/lsb-release | cut -f2 -d=) universe" >> /etc/apt/sources.list.d/sur5r-i3.list \
    && apt update && apt install -y i3 feh
# RUN setcap -r `which i3status`

# VNC+xrdp (32 MB)
RUN curl -Lv https://dl.bintray.com/tigervnc/stable/tigervnc-1.7.0.x86_64.tar.gz -o /tmp/tigervnc-1.7.0.x86_64.tar.gz \
    && tar -xvf /tmp/tigervnc-1.7.0.x86_64.tar.gz -C /tmp \
    && rsync -avz /tmp/tigervnc*/usr/ /usr \
    && apt-get update && apt-get install -y x11-xkb-utils
RUN apt-get update && apt-get install -y \
    git autoconf libtool pkg-config gcc g++ make libssl-dev libpam0g-dev libjpeg-dev libx11-dev libxfixes-dev libxrandr-dev  flex bison libxml2-dev intltool xsltproc xutils-dev python-libxml2 g++ xutils libfuse-dev libmp3lame-dev nasm libpixman-1-dev xserver-xorg-dev \
    && mkdir -p /tmp/git/neutrinolabs \
    && cd /tmp/git/neutrinolabs \
    && wget https://github.com/neutrinolabs/xrdp/releases/download/v0.9.3.1/xrdp-0.9.3.1.tar.gz \
    && tar xvfz xrdp-*.tar.gz \
    && cd /tmp/git/neutrinolabs/xrdp-* \
    && ./bootstrap \
    && ./configure --enable-fuse --enable-mp3lame --enable-pixman --enable-painter \
    && make \
    && make install \
    && ln -s /usr/local/sbin/xrdp{,-sesman} /usr/sbin
ADD xstartup /tmp/xstartup
ADD xrdp.ini /root/xrdp.ini

# rofi (11 MB)
RUN apt-get update && apt-get install -y rofi

# terminal (45 MB)
RUN apt-get update && apt-get install -y terminator

# editor (197 MB)
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list \
    && apt-get update && apt-get install -y code
    
# browser (326 MB)
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable

ADD bootstrap2.sh /tmp/bootstrap2.sh

# RUN apt-get update && apt-get install -y dunst
# RUN apt-get update && apt-get install -y rox-filer

CMD ["/usr/sbin/sshd", "-D"]

