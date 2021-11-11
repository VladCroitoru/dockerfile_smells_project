FROM nginx
MAINTAINER tym

RUN apt-get update
RUN apt-get install -y python3 python3-pip libjpeg-dev zlib1g-dev

WORKDIR /root/
ADD . .
RUN pip3 install -r requirements.txt
RUN mv nginx.conf /etc/nginx/

VOLUME /root/share/
EXPOSE 80
ENTRYPOINT ["sh", "-c", "service nginx restart && python3 app.py"]

