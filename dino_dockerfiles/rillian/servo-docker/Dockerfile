FROM fedora:latest
MAINTAINER Ralph Giles <giles@mozilla.org>

# Install tools
RUN yum install -y git which make gcc gcc-c++

# Install dependencies
RUN yum install -y glib2-devel freetype-devel fontconfig-devel
RUN yum install -y glfw-devel mesa-libGLU-devel
RUN yum install -y openssl-devel

# Check out and build
RUN git clone https://github.com/servo/servo
RUN cd servo && ./mach build
