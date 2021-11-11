FROM ubuntu:20.04
ENV TZ 'Asia/Seoul'
RUN echo $TZ > /etc/timezone && \
    apt update && apt install -y tzdata && \
    apt install wget -y && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt install python3.9 -y && \
    apt install python3-pip -y && \
    apt install -y vim && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt update && \
    apt install -y xvfb && \
    apt install -y google-chrome-stable && \
    apt install -y curl && \
    apt clean

ARG PUID
ARG PGID

RUN mkdir -p /comics-downloader

COPY . /comics-downloader

RUN chmod +x /comics-downloader/entry-point.sh
RUN chmod +x /comics-downloader/complete-noti.sh
RUN chmod +x /comics-downloader/main
RUN chown -R ${PUID}:${PGID} /comics-downloader
RUN chmod -R 775 /comics-downloader
RUN chmod -R g+s /comics-downloader

# RUN addgroup --gid ${PGID} comics
RUN groupadd -o -g ${PGID} comics
RUN adduser -u ${PUID} --disabled-password --gecos "" --force-badname --ingroup comics comics

USER comics

WORKDIR /comics-downloader

RUN python3 -m pip install --user xlrd
RUN python3 -m pip install --user pyvirtualdisplay
RUN python3 -m pip install --user -r /comics-downloader/requirements.txt

CMD ["/comics-downloader/entry-point.sh"]
