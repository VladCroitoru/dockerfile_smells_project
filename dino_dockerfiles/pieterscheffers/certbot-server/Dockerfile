FROM certbot/certbot:latest

RUN pip install Flask \
	&& mkdir -p /usr/app

EXPOSE 5000

ENTRYPOINT [ "python", "/usr/app/server.py" ]

COPY ./server.py ./cert.pem ./key.pem /usr/app/
