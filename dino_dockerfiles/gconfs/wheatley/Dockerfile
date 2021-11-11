FROM alpine
MAINTAINER Alexis Horgix Chotard <alexis.horgix.chotard@gmail.com>

ENV SOPELVER      6.3.1
ENV PYREDMINEVER  1.5.0

RUN apk add --update ca-certificates python3 \
  && wget https://bootstrap.pypa.io/get-pip.py \
  && wget https://github.com/sopel-irc/sopel/archive/${SOPELVER}.tar.gz -O sopel.tar.gz \
  && wget https://github.com/maxtepkeev/python-redmine/archive/v${PYREDMINEVER}.tar.gz -O python-redmine.tar.gz \
  && tar xzf sopel.tar.gz \
  && tar xzf python-redmine.tar.gz \
  && python3 get-pip.py \
  && pip3 install -r sopel-${SOPELVER}/requirements.txt \
  && pip3 install ipython \
  && rm sopel.tar.gz python-redmine.tar.gz get-pip.py \
  && rm -rf /tmp/* /var/cache/apk/* \
  && adduser -D sopel \
  && cd python-redmine-${PYREDMINEVER} && python3 setup.py install

COPY wheatley-docker.cfg /home/sopel/wheatley.cfg
COPY gredmine.py /home/sopel/gredmine.py
RUN chown sopel:sopel /home/sopel/*

CMD su sopel -c 'python3 /sopel-6.3.1/sopel.py -c /home/sopel/wheatley.cfg'
