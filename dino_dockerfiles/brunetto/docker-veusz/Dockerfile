# Docker image to provide Veusz
#
# Build with
#   docker build --force-rm -t brunetto/docker-veusz-1.24 .
# run with
#   docker run -e DISPLAY=<YOUR IP>:0 -i -t -v $HOME/Docker/share:/share --name veusz brunetto/docker-veusz-1.24
# or
#   use the included bash script "veusz"
#
# Thanks to
# - https://blog.jessfraz.com/post/docker-containers-on-the-desktop/
# - http://kartoza.com/how-to-run-a-linux-gui-application-on-osx-using-docker/
#

FROM ubuntu:16.04
MAINTAINER Brunetto Ziosi <brunetto.ziosi@gmail.com>

# Install needed packages.
RUN apt-get update --quiet && apt-get install --yes \
    wget git build-essential xvfb python-numpy python-sip python3-sip sip-dev pyqt4-dev-tools \
    python-pyside.qtcore python-qt4-dev libqt4-dev qt4-dev-tools python-simplejson \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Download JSON import plugin and download build and install Veusz
RUN mkdir /share \
    mkdir /plugins \
    && cd plugins \
    && wget https://raw.githubusercontent.com/brunetto/veuszPlugins/master/veuszImportJSON.py \
    && cd / \
    && git clone https://github.com/jeremysanders/veusz.git \
    && cd veusz && python setup.py build && python setup.py install \
    && cd .. && rm -rf veusz

# Uninstall unuseful packages
RUN apt-get autoremove --yes && apt-get purge --yes wget git

# Default command.
#ENTRYPOINT ["/bin/bash"]
ENTRYPOINT ["/usr/local/bin/veusz"]
CMD ["--plugin=/plugins/veuszImportJSON.py"]