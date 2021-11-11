FROM ubuntu:latest
MAINTAINER Tadashi Kamitaki "tkamitaki@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential nginx
RUN useradd -ms /bin/bash appuser
USER appuser

ENV FLASK_CONFIG_LOCATION="/app/settings.cfg"
COPY . /app
COPY ./compliment-sender.conf /etc/init/compliment-sender.conf
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]
