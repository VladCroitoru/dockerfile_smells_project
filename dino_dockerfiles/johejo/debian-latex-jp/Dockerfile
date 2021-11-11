FROM debian:stable-slim

RUN apt update && \
    apt upgrade -y && \
    apt install fonts-ipafont fonts-ipaexfont texlive texlive-formats-extra texlive-science texlive-lang-japanese -y && \
    apt purge *-doc* *chinese* *korean* *thai* -y && \
    apt clean -y && \
    apt autoremove -y && \
    apt autoclean -y && \
    mkdir /workdir

WORKDIR /workdir

VOLUME ["/workdir"]

CMD ["bash"]
