FROM ubuntu:latest
MAINTAINER boogy theboogymaster@gmail.com

LABEL Name="ubuntu/LinuxPowerShell"

ENV DEBIAN_FRONTEND noninteractive
RUN apt update \
        && apt -yq upgrade \
        && apt -yq install \
        git wget libunwind8 libicu55 libcurl3

RUN useradd --create-home --shell /bin/bash poweruser
RUN wget -q https://github.com/PowerShell/PowerShell/releases/download/v7.0.0-rc.3/powershell-lts_7.0.0-rc.3-1.ubuntu.18.04_amd64.deb -O powershell.deb \
    && dpkg -i powershell.deb \
    && apt-get install -f \
    && rm -f $_

USER poweruser

RUN mkdir -p /home/poweruser/.local/share/powershell/Modules/ \
    && git clone https://github.com/PowerShellMafia/PowerSploit.git /home/poweruser/.local/share/powershell/Modules/PowerSploit

WORKDIR /home/poweruser

CMD [ "/usr/bin/powershell" ]
