FROM intelopencl/intel-opencl:ubuntu-20.10-ppa

ENV DEBIAN_FRONTEND=noninteractive

ARG INTEL_DRIVER=l_opencl_p_18.1.0.015.tgz
ARG INTEL_DRIVER_URL=https://registrationcenter-download.intel.com/akdlm/irc_nas/vcp/15532

RUN apt update
RUN apt install apt-utils unzip tar curl xz-utils alien clinfo lsb-core libnuma-dev -q -y

RUN mkdir -p /tmp/opencl-driver-intel
WORKDIR /tmp/opencl-driver-intel
RUN echo INTEL_DRIVER is ${INTEL_DRIVER}
RUN curl -O ${INTEL_DRIVER_URL}/${INTEL_DRIVER}
RUN tar -xf ${INTEL_DRIVER}

WORKDIR /tmp/opencl-driver-intel/l_opencl_p_18.1.0.015
RUN sed -i 's/ACCEPT_EULA=decline/ACCEPT_EULA=accept/' silent.cfg
RUN ./install.sh --silent silent.cfg


WORKDIR /usr/app/agent

RUN apt update -q -y
RUN apt install pciutils tini python3 python3-pip zsh -y -q
RUN apt install intel-opencl-icd clinfo -q -y
RUN pip install psutil requests 
# RUN wget https://hashtopolis.kochie.io/agents.php?download=2 -O hashtopolis.zip
COPY hashtopolis.zip .

ENV HASHTOPOLIS_SERVER_URL=https://hashtopolis.kochie.io/api/server.php
ENV HASHTOPOLIS_VOUCHER=gyaAQnn0

ENTRYPOINT [ "tini", "-g", "-v", "--", "python3", "hashtopolis.zip"]

CMD [ "--auto-de-register", "--debug" ]
