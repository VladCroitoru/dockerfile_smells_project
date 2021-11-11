FROM python:3.4

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN pip install Flask==0.11.1 uWSGI==2.0.13.1 requests==2.11.0 redis==2.10.5
WORKDIR /app
COPY app /app
COPY run.sh /

EXPOSE 9090 9191
USER uwsgi

CMD ["/run.sh"]
