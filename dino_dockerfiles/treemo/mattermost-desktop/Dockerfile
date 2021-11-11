FROM debian


# config
ENV MATTERMOST_VERSION 3.4.1


# install
RUN apt update && apt install -y wget libgtk2.0-0 libxtst6 libxss1 libgconf-2-4 libnss3 libasound2
RUN cd /tmp && \
	wget https://releases.mattermost.com/desktop/$MATTERMOST_VERSION/mattermost-desktop-$MATTERMOST_VERSION-linux-x64.tar.gz && \
	tar xzvf mattermost-desktop-*.tar.gz && \
	mv mattermost-desktop-linux-x64/ /usr/lib/mattermost/


# clean / optimise docker size
RUN apt remove --purge -y wget
RUN apt-get autoremove -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /tmp/* /var/tmp/*


# running
ENTRYPOINT ["/usr/lib/mattermost/Mattermost"]

