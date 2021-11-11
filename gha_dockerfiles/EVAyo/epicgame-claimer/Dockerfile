FROM ubuntu

LABEL maintainer="Luminoleon <luminoleon@outlook.com>"

ENV DEBIAN_FRONTEND=noninteractive TZ=Asia/Shanghai

COPY requirements.txt install_dependencies.sh /

RUN apt update \
    && apt install -y python3 python3-pip \
    && sh ./install_dependencies.sh \
    && pip3 install --no-cache-dir -r requirements.txt \
    && pyppeteer-install \
    && apt purge -y python3-pip \
    && apt autoremove -y \
    && apt clean

COPY *.py /

ENTRYPOINT [ "python3", "-u", "main.py" ]
