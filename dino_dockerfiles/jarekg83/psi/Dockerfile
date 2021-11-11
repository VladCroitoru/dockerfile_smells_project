# Use offical Ubuntu image
FROM ubuntu:latest

# Let's add necessary packages...
RUN apt-get update -y
RUN apt-get install curl build-essential \
    qt5-default libidn2-0-dev libidn11 \ 
    libidn11-dev libqca-qt5-2-dev \
    libqt5x11extras5-dev qtmultimedia5-dev -y

# Download PSI
RUN curl -o /tmp/psi-1.3.xz https://10gbps-io.dl.sourceforge.net/project/psi/Psi/1.3/psi-1.3.tar.xz

# Compile PSI. Please take a not of -j 8 flag for make. It will create 8 gcc threads.
# If you don't have so many it can melt down your CPU ;).
RUN cd /tmp && tar xf psi-1.3.xz && cd /tmp/psi-1.3/ && \
       ./configure --prefix=/opt/psi && make -j 8 && make install

# Run PSI
CMD /opt/psi/bin/psi
