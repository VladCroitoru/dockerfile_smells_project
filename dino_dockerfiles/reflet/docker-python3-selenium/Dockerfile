FROM python:3
USER root

# system update
RUN apt-get update

# locale
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

# timezone (Asia/Tokyo)
ENV TZ JST-9

# etc
ENV TERM xterm

# add tools to work.
RUN apt-get install -y vim less

# install selenium.
RUN pip install --upgrade pip
RUN pip install selenium
