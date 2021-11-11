FROM python:3.5

# install nginx, supervisor and vim
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y ca-certificates nginx \
	&& apt-get install -y supervisor vim \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install uWSGI httpbin
RUN mkdir /log

COPY ./supervisor-app.conf /etc/supervisor/conf.d/
COPY ./nginx.conf /etc/nginx/
COPY ./uwsgi.ini /app/

EXPOSE 80
CMD ["supervisord", "-n"]
