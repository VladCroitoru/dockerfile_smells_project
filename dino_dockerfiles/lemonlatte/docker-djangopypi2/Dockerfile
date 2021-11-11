# DjangoPypi Server

FROM ubuntu:13.10
MAINTAINER Jim Yeh <lemonlatte@gmail.com>

RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -sf /bin/true /sbin/initctl
RUN ln -sf /bin/false /usr/sbin/policy-rc.d

RUN apt-get update -y
RUN apt-get -y -q install python-dev python-pip git supervisor nginx
RUN pip install uwsgi virtualenv
RUN virtualenv pypi-site
RUN /bin/bash -c 'source pypi-site/bin/activate && pip install djangopypi2'
RUN /bin/bash -c 'source pypi-site/bin/activate && DJANGOPYPI2_ROOT=/pypi-site/djangopypi2 manage-pypi-site syncdb --noinput'
RUN /bin/bash -c 'source pypi-site/bin/activate && DJANGOPYPI2_ROOT=/pypi-site/djangopypi2 manage-pypi-site collectstatic --noinput'
RUN /bin/bash -c 'source pypi-site/bin/activate && DJANGOPYPI2_ROOT=/pypi-site/djangopypi2 manage-pypi-site loaddata initial'

ADD setup_script.py pypi-site/
RUN /bin/bash -c 'source pypi-site/bin/activate && python pypi-site/setup_script.py'
RUN rm pypi-site/setup_script.py

RUN echo 'daemon off;' >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default

ADD uwsgi.ini pypi-site/
ADD wsgi.py pypi-site/
ADD settings.json pypi-site/djangopypi2/
ADD pypi-site /etc/nginx/sites-enabled/
ADD supervisor.conf/ /etc/supervisor/conf.d/
RUN chown www-data:www-data -R pypi-site/djangopypi2
VOLUME /var/data

EXPOSE 80
ADD run_server.sh run_server.sh
CMD ["sh", "run_server.sh"]
