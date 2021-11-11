FROM python:3.4

RUN useradd uwsgi
#RUN pip install Flask==0.10.1 uWSGI==2.0.8 requests==2.5.1
RUN pip install Flask uWSGI requests redis
WORKDIR /app
COPY app /app
COPY cmd.sh /

EXPOSE 9090 9091
USER uwsgi

CMD ["/cmd.sh"]
