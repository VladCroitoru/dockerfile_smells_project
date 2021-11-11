FROM python:3.4

RUN groupadd -r uwsgi && useradd -rg uwsgi uwsgi
RUN pip install --upgrade pip
RUN pip install Flask==0.10.1 uWSGI==2.0.8 requests==2.5.1 redis==2.10.3
WORKDIR /app
copy app /app
copy cmd.sh /

EXPOSE 9090 9091
USER uwsgi

CMD ["/cmd.sh"]
