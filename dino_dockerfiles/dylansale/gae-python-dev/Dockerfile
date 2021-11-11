FROM python:2.7-slim

MAINTAINER dylan.sale@gmail.com

RUN mkdir /code
WORKDIR /code

RUN apt-get -y update \
&& apt-get install -y unzip \
&& apt-get install -y -qq --no-install-recommends python-mysqldb \
&& apt-get clean

#Setup the python path so that it finds the MySQLdb dist package
#(not setup by default on python dockerfile for some reason)
ENV PYTHONPATH $PYTHONPATH:/usr/lib/python2.7/dist-packages

ADD https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.24.zip /tmp/gae.zip
RUN printf "opt_in: false\ntimestamp: 0.0" > /.appcfg_nag
RUN cd /usr/local && unzip /tmp/gae.zip && rm /tmp/gae.zip
ENV PATH $PATH:/usr/local/google_appengine/

CMD ["dev_appserver.py", "/code"]

