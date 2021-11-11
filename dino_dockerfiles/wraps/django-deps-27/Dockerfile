FROM python:2.7

RUN set -ex \
    && echo "deb http://toolbelt.heroku.com/ubuntu ./" > /etc/apt/sources.list.d/heroku.list \
    && wget -O- https://toolbelt.heroku.com/apt/release.key | apt-key add - \
    && apt-get update \
    && apt-get install -y heroku-toolbelt ruby ruby-dev \
    && gem install dpl \
    && useradd --create-home proj \
    && chown -R proj:proj /var/lib/gems/2.1.0

USER proj
WORKDIR /home/proj

RUN mkdir -p /home/proj/.virtualenvs/ \
    && pip install -U pip virtualenv \
    && virtualenv /home/proj/.virtualenvs/proj \
    && . /home/proj/.virtualenvs/proj/bin/activate
ENV PATH /home/proj/.virtualenvs/proj/bin:$PATH
