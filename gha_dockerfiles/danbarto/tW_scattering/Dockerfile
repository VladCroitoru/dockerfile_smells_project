FROM rootproject/root:6.22.00-conda

# Build the image as root user
USER root

RUN apt-get -qq -y update && \
    apt-get -qq -y upgrade && \
    apt-get -qq -y install vim && \
    apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt-get/lists/*
RUN pip3 install --upgrade numpy && \
    pip3 install --upgrade matplotlib && \
    pip3 install uproot coffea jupyter tqdm pandas backports.lzma pyyaml klepto && \
    pip3 install --upgrade tqdm

COPY . /tW_scattering
WORKDIR /tW_scattering

RUN echo "export PYTHONPATH=${PYTHONPATH}:/tW_scattering" >> ~/.bashrc

# Run as docker user by default when the container starts up
#USER docker
