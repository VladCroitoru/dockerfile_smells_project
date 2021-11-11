FROM autodomotalus/java7

MAINTAINER Autodomotalus <https://github.com/autodomotalus>

RUN apt-get update

# Download Android Studio 2.2.3.0
RUN curl 'https://dl.google.com/dl/android/studio/ide-zips/2.2.3.0/android-studio-ide-145.3537739-linux.zip' > /tmp/studio.zip && unzip -d /opt /tmp/studio.zip && rm /tmp/studio.zip

# Install librairies
RUN apt-get install -y lib32z1 lib32ncurses5 lib32bz2-1.0 lib32stdc++6
#libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 libbz2-1.0:i386


# Install X11
RUN apt-get install -y x11-apps

# Clean up
RUN apt-get clean
RUN apt-get purge

# Set up permissions for X11 access.
RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer

CMD /opt/android-studio/bin/studio.sh
