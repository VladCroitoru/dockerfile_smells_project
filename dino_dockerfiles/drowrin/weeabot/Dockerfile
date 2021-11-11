FROM weeabot_base

ADD . /weeabot
WORKDIR /weeabot

VOLUME /weeabot/status
VOLUME /weeabot/config
VOLUME /weeabot/images

CMD python3.6 -u Weeabot.py
