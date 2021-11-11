FROM python:2.7-onbuild
MAINTAINER megane42

RUN apt-get update
RUN apt-get install -y imagemagick
RUN apt-get install -y libmagickwand-dev
RUN apt-get install -y ghostscript

ENV TZ=Asia/Tokyo

CMD python kyoko.py