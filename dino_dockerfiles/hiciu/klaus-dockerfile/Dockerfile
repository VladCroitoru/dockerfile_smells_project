FROM debian

# see https://github.com/oddbloke/klaus-dockerfile
MAINTAINER Krzysztof Warzecha <kwarzecha7@gmail.com>

# see https://www.google.pl/search?q=eatmydata+docker
# This forces dpkg not to call sync() after package extraction and speeds up install
# (we are also using eatmydata for that, I'm not sure if this is nessecary)
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup

# do not install recommended / suggested packages, always assume "yes", do not cache packages
ADD apt-config /etc/apt/apt.conf.d/docker-config

RUN apt-get update && apt-get install eatmydata

RUN eatmydata apt-get install \
    virtualenv git exuberant-ctags python libpython2.7

RUN virtualenv /opt/klaus/venv
RUN /opt/klaus/venv/bin/pip install wheel

# you can also use locally built wheels by mounting volume with them under /wheelhouse and overriding that variable
ARG WHEELHOUSE_URL=https://hiciu.org/docker/klaus-dockerfile/wheelhouse/
ADD wheelhouse /wheelhouse

# install
RUN /opt/klaus/venv/bin/pip install --no-index --find-links=$WHEELHOUSE_URL \
    klaus markdown docutils uwsgi python-ctags ldap3 expiringdict chardet

WORKDIR /opt/klaus
ADD wsgi_autoreload_ctags.py wsgi_autoreload_ctags.py
ADD wsgi_autoreload_ctags_ldap.py wsgi_autoreload_ctags_ldap.py

EXPOSE 8080

VOLUME /srv/git

ENV KLAUS_REPOS_ROOT /srv/git/
ENV KLAUS_SITE_NAME "klaus"

# you can set this to "none" or "tags-and-branches"
# ee tags-and-brancheshttps://github.com/jonashaag/klaus/wiki/Enable-ctags-support
ENV KLAUS_CTAGS_POLICY "tags-and-branches"

# uwsgi will switch to that uid before running klaus
ENV UWSGI_SETUID 1000

ENV UWSGI_WSGI_FILE wsgi_autoreload_ctags.py

# feel free to override these
CMD /opt/klaus/venv/bin/uwsgi --uid $UWSGI_SETUID --wsgi-file $UWSGI_WSGI_FILE --http 0.0.0.0:8080 --processes 4 --threads 2
