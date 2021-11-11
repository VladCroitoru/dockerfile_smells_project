FROM phusion/baseimage:latest

ENV USER steam
ENV HOME /home/$USER
ENV SERVER $HOME/server
ENV SOURCE $HOME/source

RUN dpkg --add-architecture i386 \
    && apt-get -y update \
    && apt-get install -y software-properties-common python-software-properties \
    && add-apt-repository ppa:jonathonf/python-3.6 \
    && apt-get -y update \
    && apt-get -y install lib32gcc1 wget net-tools lib32stdc++6 zlib1g:i386 libffi6:i386 python3.6 python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && useradd -m $USER

USER $USER
RUN mkdir $SERVER && cd $SERVER \
    && wget http://media.steampowered.com/client/steamcmd_linux.tar.gz \
    && tar -xvzf steamcmd_linux.tar.gz && rm steamcmd_linux.tar.gz \
    && ./steamcmd.sh +login anonymous +force_install_dir ./csgo +app_update 740 validate +quit \
    && mkdir $HOME/.steam/sdk32 \
    && ln -s $SERVER/linux32/steamclient.so $HOME/.steam/sdk32/steamclient.so

COPY source-python $SOURCE

RUN cp -r $SOURCE/addons $SERVER/csgo/csgo/ \
    && cp -r $SOURCE/cfg $SERVER/csgo/csgo/ \
    && cp -r $SOURCE/logs $SERVER/csgo/csgo/ \
    && cp -r $SOURCE/resource $SERVER/csgo/csgo/ \
    && cp -r $SOURCE/sound $SERVER/csgo/csgo/

COPY requirements.txt $HOME

RUN pip3 install --upgrade pip==9.0.3 \
    && pip3 install -t $SERVER/csgo/csgo/addons/source-python/packages/custom/ -r $HOME/requirements.txt

EXPOSE 27015

WORKDIR $SERVER/csgo

ENTRYPOINT ["./srcds_run"]
