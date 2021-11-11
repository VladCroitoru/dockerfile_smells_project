# Runs fiovisualizer in Docker over an HTML5 VNC connection
# Forked from dit4c/dockerfile-dit4c-container-x11

FROM dit4c/dit4c-container-base:latest
MAINTAINER github.com/sammcj

# Install
# - MESA DRI drivers for software GLX rendering
# - X11 dummy & void drivers
# - X11 xinit binary
# - reasonable fonts for UI
# - x11vnc
# - python-websockify
# - openbox
# - xterm
RUN rpm --rebuilddb && \
  fsudo yum install -y \
    mesa-dri-drivers \
    xorg-x11-drv-dummy \
    xorg-x11-drv-void \
    xorg-x11-xinit \
    dejavu-sans-fonts \
    dejavu-sans-mono-fonts \
    dejavu-serif-fonts \
    x11vnc \
    python-websockify \
    openbox \
		numpy \
		PyQt4 \
		fio \
    xterm && \
  rm -f /usr/share/applications/x11vnc.desktop

# Get the last good build of noVNC
RUN git clone https://github.com/kanaka/noVNC.git /opt/noVNC && \
    cd /opt/noVNC && \
    git checkout 8f3c0f6b9b5e5c23a7dc7e90bd22901017ab4fc7

# Install latest tint2 & lxrandr from RPM and icons from Yum
RUN rpm --rebuilddb && \
  fsudo yum localinstall -y https://kojipkgs.fedoraproject.org/packages/tint2/0.12/4.fc21/x86_64/tint2-0.12-4.fc21.x86_64.rpm && \
  fsudo yum localinstall -y https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide/x86_64/os/Packages/l/lxrandr-0.3.0-1.fc23.x86_64.rpm && \
  fsudo yum install -y gnome-icon-theme

# Add supporting files (directory at a time to improve build speed)
COPY etc /etc
COPY var /var

# Add python requirements

RUN cd /tmp && wget -O - http://www.pyqtgraph.org/downloads/pyqtgraph-0.9.10.tar.gz | tar fxvz - && \
		cd pyqtgraph* && fsudo python setup.py install

RUN cd /tmp && wget -O - http://cython.org/release/Cython-0.23.tar.gz | tar fxvz - && \
	  cd Cython* && fsudo python setup.py install

RUN git clone https://github.com/01org/fiovisualizer.git /home/researcher/fiovisualizer

# Because COPY doesn't respect USER...
USER root
RUN chown -R researcher:researcher /etc /var
USER researcher

EXPOSE 8080

# Check nginx config is OK
RUN nginx -t
