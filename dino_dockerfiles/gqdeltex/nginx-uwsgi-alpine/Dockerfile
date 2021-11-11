FROM alpine
RUN apk add --no-cache --update python python-dev py-pip build-base linux-headers nginx
RUN pip install uwsgi
RUN mkdir /app/
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./start.sh /
EXPOSE 80
CMD "./start.sh"
