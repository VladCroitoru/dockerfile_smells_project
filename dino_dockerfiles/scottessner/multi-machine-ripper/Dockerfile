# Start with latest LTS of Ubuntu
FROM ubuntu:latest

# Install basic dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    # udev \
    software-properties-common \
    python3 \
    python3-pip \
    python3-dev \
    gcc \
    git

# After we installed software-properties-common, now we can add our ppa's for handbrake
RUN add-apt-repository ppa:stebbins/handbrake-releases \
    && add-apt-repository ppa:mc3man/xerus-media

# Install software from ppa's
RUN apt-get update && apt-get install -y --no-install-recommends \
    handbrake-cli \
    libavcodec-extra

RUN mkdir -p /data/incoming
RUN mkdir -p /data/outgoing
RUN mkdir -p /log

# Set up directory and download software
WORKDIR /app

ADD . /app

# Set up udev to watch for optical drive changes
#RUN ln -s /app/51-automedia.rules /lib/udev/rules.d/ \
#    && service udev restart


# Set up links to refer to python3 versions of python and pip
RUN cd /usr/bin \
    && ln -s python3 python \
    && ln -s pip3 pip

# Copy systemd service to the appropriate folder
#RUN cp /app/mmr@.service /etc/systemd/system/

# Need to install setuptools to build from source distributions
RUN pip install setuptools

#RUN cd /opt \
#    && git clone https://github.com/scottessner/multi-machine-ripper.git

# Install python requirements
RUN pip install -r requirements.txt

EXPOSE 1900
EXPOSE 22

CMD ["python", "run.py", "1900"]





