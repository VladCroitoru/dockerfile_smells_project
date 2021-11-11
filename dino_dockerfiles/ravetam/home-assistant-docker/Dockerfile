FROM python:3.9.1-alpine3.13
LABEL maintainer="Lazcad <support@lazcad.com>"

VOLUME /config
ENV CRYPTOGRAPHY_ALLOW_OPENSSL_102 1
RUN apk add --no-cache --update bash git gcc g++ musl-dev linux-headers curl make libffi-dev openssl-dev libjpeg-turbo-dev zlib-dev \
    libssl1.1  libxml2-dev libxslt libxslt-dev ffmpeg && \
    rm -rf /root/.cache /var/cache/apk/*

RUN pip3 install --no-cache-dir --upgrade homeassistant==2021.5.5 \
                                          PyMySQL \
                                          aiohttp_cors==0.7.0 distro==1.5.0 \ 
                                          pillow==8.1.2 icmplib==2.1.1 defusedxml==0.6.0 \
                                          home-assistant-frontend==20210504.0 \
                                          mutagen==1.45.1 netdisco==2.8.2 slixmpp==1.7.0 sqlalchemy==1.4.13 xmltodict==0.12.0 \
                                          zeroconf==0.29.0 colorlog==5.0.1 plexapi==4.5.1 plexauth==0.0.6 plexwebsocket==0.0.13 \
                                          PyXiaomiGateway==0.13.4 pysonos==0.0.47 \
                                          python-miio==0.5.6 yeelight==0.6.2 broadlink==0.17.0 aiohue==2.3.1 \
                                          pyowm==3.2.0 slackclient==2.5.0 feedparser==6.0.2 \
                                          construct==2.10.56 paho-mqtt==1.5.1 alpha_vantage==2.3.1 \
                                          PyQRCode==1.2.1 pyotp==2.3.0 aioesphomeapi==2.6.6 python-forecastio==1.4.0 \
                                          wakeonlan==2.0.1 aioftp==0.12.0 PyNaCl==1.3.0 hass-nabucasa==0.43.0 \
                                          HAP-python==3.4.1 beautifulsoup4==4.9.3 blockchain==1.4.4 jsonpath==0.82 \
                                          sonarr==0.3.0 pynzbgetapi==0.2.0 pymsteams==0.1.12 \
                                          caldav==0.7.1 workalendar zeep[async]==4.0.0 WSDiscovery==2.0.0 \
                                          git+https://github.com/tam-wh/python-onvif-zeep-async.git#egg=onvif-zeep-async

                                          # av==8.0.3  not possible on alpine

EXPOSE 8123

CMD [ "hass", "--config", "/config" ]
