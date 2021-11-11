FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY ./app /app
COPY ./jpsanford.conf /etc/nginx/conf.d/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80 443
VOLUME /etc/letsencrypt