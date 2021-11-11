FROM suchja/wine:dev

USER root

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs git zip genisoimage
RUN apt-get clean

# Wine really doesn't like to be run as root, so let's use a non-root user
USER xclient
ENV HOME /home/xclient
ENV WINEPREFIX /home/xclient/.wine
ENV WINEARCH win32
RUN wine wineboot --init

# Use xclient's home dir as working dir
WORKDIR /home/xclient

RUN echo "alias winegui='wine explorer /desktop=DockerDesktop,1024x768'" > ~/.bash_aliases 
