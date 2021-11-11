FROM ubuntu
MAINTAINER Jim Yeh <lemonlatte@gmail.com>

RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl
RUN ln -sf /bin/false /usr/sbin/policy-rc.d

RUN apt-get update -y
RUN apt-get -y -q install python-pip git python-dev
RUN pip install virtualenv

RUN git clone --recursive git://github.com/mozilla/moztrap
RUN cd /moztrap && git checkout 1.5.4

RUN apt-get install -y libmysqlclient-dev build-essential mysql-client
RUN apt-get install -y supervisor nginx memcached
RUN apt-get clean

RUN pip install uwsgi

COPY moztrap moztrap/
WORKDIR /moztrap
RUN virtualenv .venv
RUN ./with_venv.sh ./bin/install-reqs
RUN ./with_venv.sh ./manage.py collectstatic --noinput
RUN chown -R www-data /moztrap

WORKDIR /

ADD moztrap-init.sh /
ADD moztrap-nginx /etc/nginx/sites-enabled/
ADD moztrap-supervisor.conf /etc/supervisor/conf.d/
ADD moztrap-add-user.sh /
ADD moztrap-uwsgi.ini /
ADD run.sh /

EXPOSE 8000
CMD ["/usr/bin/supervisord", "-n"]

