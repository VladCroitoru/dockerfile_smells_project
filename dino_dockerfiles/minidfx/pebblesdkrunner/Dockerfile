# I migrate to alpine soon as gcc-arm-embedded can be
# compiled
FROM ubuntu:latest
MAINTAINER Burgy Benjamin <https://twitter.com/minidfx>

# Which versions?
ENV SDKVER 4.3
ENV TOOLVER v4.5

# Fix the python result piped to another script
ENV PYTHONIOENCODING=utf-8

# Ignore any console dialogs
ENV DEBIAN_FRONTEND=noninteractive

# To be able to remove the sudo command
ENV SUDO_FORCE_REMOVE=yes

# Install Pebble dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:team-gcc-arm-embedded/ppa && \
    apt-get update && \
    apt-get install -y curl \
                       git \
                       python \
                       python-dev \
                       libfreetype6-dev \
                       nodejs \
                       npm \
                       gcc-arm-embedded \
                       sudo && \
    curl -s https://bootstrap.pypa.io/get-pip.py | python -

# Create the Pebble user
RUN useradd -m -U pebble && \
    mkdir -p /home/pebble/.pebble-sdk && \
    mkdir -p /home/pebble/project
RUN chown -R pebble:pebble /home/pebble

# Clone the Pebble tool
RUN git clone -b $TOOLVER https://github.com/pebble/pebble-tool.git /home/pebble/tool
RUN chown -R pebble:pebble /home/pebble

# Install the python dependencies
WORKDIR /home/pebble/tool
RUN pip install -r requirements.txt virtualenv sh
RUN sudo -EH -u pebble virtualenv .env && \
    sudo -EH -u pebble /bin/bash -c "source .env/bin/activate && \
				     pip uninstall -y six && \
                                     pip install six==1.9.0 && \
                                     pip install -r requirements.txt && \
                                     deactivate" && \
    mkdir -p /home/pebble/.pebble-sdk && \
    sudo -u pebble touch /home/pebble/.pebble-sdk/ENABLE_ANALYTICS

# Install the Pebble SDK
RUN chown -R pebble:pebble /home/pebble
RUN sudo -EH -u pebble yes | sudo -EH -u pebble python pebble.py sdk install $SDKVER

# Clean up
RUN apt-get remove -y --purge sudo && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/apt/cache && \
    rm -rf /root/.cache && \
    rm -rf /home/pebble/.cache

# Set the Pebble user as default
USER pebble

# Set the project folder as default working directory
WORKDIR /home/pebble/project
VOLUME  /home/pebble/project

# Force to use the pebble tool
ENTRYPOINT ["/usr/bin/python", "/home/pebble/tool/pebble.py"]

# Set the default argument
CMD ["--help"]
