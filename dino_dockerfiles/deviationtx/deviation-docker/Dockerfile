FROM ubuntu:14.04
MAINTAINER PhracturedBlue <deviationtx@gmail.com>
RUN apt-get update && apt-get install -y build-essential git mingw32 mingw32-binutils mingw32-runtime gettext zip python python-newt
RUN cd /opt && curl --retry 10 --retry-max-time 120 -L 'https://developer.arm.com/-/media/Files/downloads/gnu-rm/8-2018q4/gcc-arm-none-eabi-8-2018-q4-major-linux.tar.bz2' | tar xfj -
CMD ["/root/build_init.sh"]
RUN mv /root /opt/root && ln -s /opt/root /root && chmod 755 /opt/root
RUN ln -s /opt/docker /home/docker
RUN echo "docker         ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers
COPY build.py /root/
COPY build_init.sh /root/
RUN sha1sum /root/build.py > /root/.build.py.sha1
VOLUME /opt
VOLUME /git
VOLUME /release


# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
