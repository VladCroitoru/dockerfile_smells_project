FROM buildpack-deps:sid
MAINTAINER Tibor Sári <tiborsari@gmx.de>

# We need wget to download the custom version of Firefox, xvfb to have a virtual screen and Firefox so all necessary libraries are installed.
RUN apt-get update -qqy && \
    apt-get install --no-install-recommends -qqy \
        ca-certificates \
        hicolor-icon-theme \
        libasound2 \
        libdbus-glib-1-2 \
        libgl1-mesa-dri \
        libgl1-mesa-glx \
        libglib2.0-0 \
        libgtk-3-0 \
        libpango1.0-0 \
        libstdc++5 \
        libv4l-0 \
        sudo \
        wget \
        xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# add entrypoint script, that will run all commands as user, that is provided on docker run
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Set up the command arguments
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["echo", "Add your command on docker run!"]