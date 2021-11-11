FROM debian:stretch
LABEL maintainer="exotime <exotime@users.noreply.github.com>"
LABEL version="0.1.1"

# The URL to fetch. Now redirects to the latest version.
ENV URL https://discordapp.com/api/download?platform=linux&format=deb

# To run the container:
# $ xhost local:docker
#
# $ docker run -it \
#       -v /tmp/.X11-unix:/tmp/.X11-unix \
#       -v /etc/localtime:/etc/localtime:ro \
#       -v ${HOME}/.config/discord/:/root/.config/discord/ \
#       -e DISPLAY=$DISPLAY \
#       --device /dev/snd \
#       exotime/discord-client-docker

RUN apt update && \
    apt install --yes --no-install-recommends \
        apt-utils \
        dbus-x11 \
        dunst \
        hunspell-en-us \
        python3-dbus \
        software-properties-common \
        libx11-xcb1 \
        gconf2 \
        libgtk2.0-0 \
        libxtst6 \
        libnss3 \
        libasound2 \
        libc++1 \
        libatomic1 \
        libnotify4 \
        libappindicator1 \
        wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget $URL -O discord.deb && \
    dpkg -i discord.deb && \
    rm discord.deb

CMD ["discord"]
