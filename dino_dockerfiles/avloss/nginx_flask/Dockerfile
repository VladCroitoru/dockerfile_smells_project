FROM debian:jessie

ADD http://nginx.org/keys/nginx_signing.key /nginx_signing.key
RUN apt-key add nginx_signing.key
RUN rm /nginx_signing.key

RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y wget bzip2 nginx

RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh \
    && bash Miniconda2-latest-Linux-x86_64.sh -b -p /anaconda2 \
    && rm Miniconda2-latest-Linux-x86_64.sh

RUN ln -s /anaconda2/bin/python /usr/bin/python
RUN ln -s /anaconda2/bin/conda /usr/bin/conda
RUN ln -s /anaconda2/bin/pip /usr/bin/pip

RUN conda install -y flask

RUN apt-get install -y build-essential
RUN pip install uwsgi
RUN ln -s /anaconda2/bin/uwsgi /usr/bin/uwsgi

COPY serving_conf/app_nginx.conf /etc/nginx/conf.d/
RUN rm /etc/nginx/conf.d/default.conf
COPY serving_conf/app_uwsgi.ini /app_uwsgi.ini
RUN mkdir /app_logs

COPY flask_app /flask_app

EXPOSE 80
COPY serving_conf/startup_script.sh /startup_script.sh
CMD bash /startup_script.sh