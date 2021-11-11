FROM python:3.9

# ENV DEBIAN_FRONTEND noninteractive
# ENV GECKODRIVER_VER v0.29.0
# ENV FIREFOX_VER 87.0

RUN apt update
RUN apt upgrade -y
RUN apt install -y \
       firefox-esr
RUN pip install  \
       requests \
       selenium \
       flask \
       gunicorn \
       google-cloud-storage

WORKDIR /app
COPY . ./
RUN chmod +x ./config/geckodriver

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app

RUN ls \config
RUN ls

#RUN pip install -r requirements.txt

# Add latest Firefox
# RUN set -x \
#    && apt install -y \
#        libx11-xcb1 \
#        libdbus-glib-1-2 \
#    && curl -sSLO https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2 \
#    && tar -jxf firefox-* \
#    && mv firefox /opt/ \
#    && chmod 755 /opt/firefox \
#    && chmod 755 /opt/firefox/firefox
#
# # Add geckodriver
# RUN set -x \
#    && curl -sSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
#    && tar zxf geckodriver-*.tar.gz \
#    && mv geckodriver /usr/bin/
#
# #COPY ./app /app
#
# #WORKDIR /app
#
# CMD python main.py
