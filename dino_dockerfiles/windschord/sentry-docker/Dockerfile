FROM centos
 
MAINTAINER windschord

RUN yum install -y gcc python-devel python-setuptools
RUN easy_install -UZ sentry
RUN /usr/bin/sentry init /etc/sentry.conf.py
RUN /usr/bin/sentry --config=/etc/sentry.conf.py upgrade

EXPOSE 9000

CMD ["/usr/bin/sentry", "--config=/etc/sentry.conf.py", "start"]