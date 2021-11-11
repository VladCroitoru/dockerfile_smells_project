FROM ubuntu:16.04
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install nginx texlive texlive-xetex supervisor nodejs-legacy npm python3 python3-pip git python3-setuptools redis-server wget unzip fontconfig

RUN wget https://fonts.google.com/download?family=Roboto
RUN unzip download?family=Roboto
RUN mkdir -p /usr/share/fonts/truetype/Roboto
RUN mv Roboto* /usr/share/fonts/truetype/Roboto
RUN fc-cache -f > /dev/null

ADD requirements.txt .
RUN pip3 install -r requirements.txt

RUN mkdir /invoicegen
ADD . /invoicegen
WORKDIR /invoicegen

RUN adduser --disabled-password --gecos '' workeruser
RUN npm install bower -g

RUN cp config/supervisord.conf /etc/supervisor.conf

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/*
RUN cp config/nginx_invoicegen.conf /etc/nginx/sites-available/invoicegen.conf
RUN ln -s /etc/nginx/sites-available/invoicegen.conf /etc/nginx/sites-enabled/invoicegen.conf
EXPOSE 80

CMD ["./docker-entrypoint.sh"]