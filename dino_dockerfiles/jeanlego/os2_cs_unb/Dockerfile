# This Dockerfile is used to build an headles vnc image based on Fedora with cloud9
FROM fedora:latest

# ------------------------------------------------------------------------------
# Install base
RUN dnf -y update '*' --refresh && \
dnf install -y glibc-static tmux python libevent-devel ncurses-devel clang perl-List-MoreUtils \
time @development-tools @virtualization zip clang curl git libxml++-devel libX11-devel libXft-devel fontconfig \
cairo-devel automake cmake flex bison ctags gdb perl valgrind vim sudo wget which net-tools bzip2 \
gdb-gdbserver numpy tigervnc-server python novnc python3-websockify python3-numpy gettext nasm \
qemu firefox

ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

RUN dnf -y -x gnome-keyring --skip-broken groups install "Xfce" && dnf -y groups install "Fonts"
RUN dnf erase -y *power* *screensaver* && rm /etc/xdg/autostart/xfce-polkit* && /bin/dbus-uuidgen > /etc/machine-id

RUN ln -s /lib64 /usr/lib/x86_64-linux-gnu

# ------------------------------------------------------------------------------
# Install Node.js
RUN curl -L https://raw.githubusercontent.com/c9/install/master/install.sh | bash
RUN dnf install -y nodejs

# ------------------------------------------------------------------------------
# Install Cloud9
RUN git clone https://github.com/c9/core.git /cloud9
RUN /cloud9/scripts/install-sdk.sh
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js

# ------------------------------------------------------------------------------
#cleanup
RUN dnf clean all

# ------------------------------------------------------------------------------
# workspace
RUN mkdir -p /workspace

# ------------------------------------------------------------------------------
# boot script
ENV USERNAME="root"
ENV PASSWORD="letmein"
ENV CLOUD9_ROOT_FOLDER="/workspace"

ADD startup.sh /
RUN chmod +x startup.sh

# ------------------------------------------------------------------------------
# expose port and directory
VOLUME /workspace
EXPOSE 8080 5901 6901

ENTRYPOINT ["/bin/sh", "startup.sh"]
