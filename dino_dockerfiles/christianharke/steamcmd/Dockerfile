FROM ubuntu:18.04
LABEL maintainer="Christian Harke <ch.harke@gmail.com>"

# Install requirements
RUN apt-get update --quiet && \
    apt-get upgrade --quiet --yes && \
    apt-get install --quiet --yes \
        lib32gcc1 \
        wget

# Switch user
ENV user steam
RUN useradd -m ${user}
USER ${user}

# Prepare environment
ENV appdir /home/${user}/Steam
RUN mkdir -p ${appdir}
WORKDIR ${appdir}

# Install application
RUN wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz && \
        tar -xvzf steamcmd_linux.tar.gz && \
        ./steamcmd.sh +quit

ENTRYPOINT ["./steamcmd.sh"]
