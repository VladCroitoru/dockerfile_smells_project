FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install --default-timeout=100 -r requirements.txt
EXPOSE 8181
VOLUME /app/app
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
