FROM andriyp/lazarus

ENV VER=${VER:-master} \
    REPO=https://github.com/twhtanghk/freeship-plus-in-lazarus \
    APP=/usr/src/app

ADD packagefiles.xml /root/.lazarus/

WORKDIR $APP

RUN apt-get update \
&&  apt-get install -y libqt4pas-dev \
&&  rm -rf /var/lib/apt/lists/* \
&&  git clone -b $VER $REPO $APP \
&&  lazbuild FreeShip.lpi

CMD ./FreeShip
