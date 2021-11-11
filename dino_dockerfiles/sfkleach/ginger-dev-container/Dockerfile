FROM ubuntu:16.10
MAINTAINER Stephen Leach "sfkleach@gmail.com"
ENV REFRESHED_AT 2017-11-16
RUN apt-get update && apt-get upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git sudo make curl

# Cloning https://github.com/Spicery/ginger.git into /var/projects/Spicery/ginger
RUN mkdir -p /var/projects/Spicery/ginger
WORKDIR /var/projects/Spicery/ginger
RUN git clone https://github.com/Spicery/ginger.git .
RUN git checkout --track origin/development
RUN make -f JumpStart.makefile ubuntu
RUN make -f JumpStart.makefile build
RUN make install-as-is
RUN tar cf - . | gzip > ../ginger-ready-to-go.tgz

# And now set up the initial user.
RUN useradd -G sudo --create-home --shell /bin/bash gdev
RUN echo "gdev:gdev" | chpasswd
WORKDIR /home/gdev

# Make that user special
RUN echo "gdev ALL=(root) NOPASSWD: ALL" >> /etc/sudoers

# Set up the mount point
ENV SPICERY_DEV_HOME=/spicery
ENV GINGER_DEV_HOME=/spicery/ginger
RUN mkdir -p ${GINGER_DEV_HOME}
RUN chown -R gdev:gdev ${SPICERY_DEV_HOME}
USER gdev
RUN echo 'export PS1="🐳 "${PS1}' >> /home/gdev/.bashrc
COPY startup.bsh /home/gdev
CMD /bin/bash startup.bsh; /bin/bash
