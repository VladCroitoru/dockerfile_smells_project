FROM    ubuntu:14.04 
MAINTAINER Yannick Saint Martino

RUN mkdir -p /usr/share/icons/hicolor/16x16/apps/
RUN mkdir -p /usr/share/icons/hicolor/32x32/apps/
RUN mkdir -p /usr/share/icons/hicolor/48x48/apps/
RUN mkdir -p /usr/share/icons/hicolor/128x128/apps/
RUN mkdir -p /usr/share/icons/hicolor/256x256/apps/

RUN apt-get update && apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository ppa:webupd8team/sublime-text-2 && apt-get update && apt-get install -y sublime-text && apt-get install -y libglib2.0-dev libx11-dev libgtk2.0-0
RUN rm -rf /var/lib/apt/lists/*

# Set locale to UTF8
RUN locale-gen --no-purge en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8
RUN dpkg-reconfigure locales
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8 


RUN export uid=1000 gid=1000 && \
    mkdir -p /home/sublimeuser && \
    echo "sublimeuser:x:${uid}:${gid}:Developer,,,:/home/sublimeuser:/bin/bash" >> /etc/passwd && \
    echo "sublimeuser:x:${uid}:" >> /etc/group && \
    echo "sublimeuser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/sublimeuser && \
    chmod 0440 /etc/sudoers.d/sublimeuser && \
    chown ${uid}:${gid} -R /home/sublimeuser

RUN mkdir -p '/home/sublimeuser/.config/sublime-text-2/Packages'
RUN mkdir -p '/home/sublimeuser/.config/sublime-text-2/Installed Packages' && cd '/home/sublimeuser/.config/sublime-text-2/Installed Packages'
RUN wget https://sublime.wbond.net/Package%20Control.sublime-package
RUN mv 'Package Control.sublime-package' '/home/sublimeuser/.config/sublime-text-2/Installed Packages/'

RUN chmod 777 -R /home/sublimeuser

# share workspace directory
VOLUME ["/workspace"]

# launch
USER sublimeuser
CMD sublime-text
