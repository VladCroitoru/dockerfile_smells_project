FROM apluslms/grade-python:3.7-3.2.3-3.0

ENV LANG C.UTF-8

RUN apt_install \
    firefox-esr \
    wbritish \
    xauth \
    xvfb \
 && :

ARG GECKO_VER=0.26.0

RUN curl -SLO https://github.com/mozilla/geckodriver/releases/download/v$GECKO_VER/geckodriver-v$GECKO_VER-linux64.tar.gz \
  && tar zxvf geckodriver-v$GECKO_VER-linux64.tar.gz \
  && mv geckodriver /usr/local/bin/ \
  && rm geckodriver-v$GECKO_VER-linux64.tar.gz

ADD requirements.txt /root
RUN pip3 install -r /root/requirements.txt \
  && rm -rf /root/.cache

ADD bin /usr/local/bin
ADD assets /assets
