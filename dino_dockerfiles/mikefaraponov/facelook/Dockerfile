FROM ubuntu:14.04

RUN apt-get update && apt-get install --force-yes -y \
    git \
    python \
    build-essential \
    python-pip \
    python-dev \
    libopencv-dev \
    python-opencv \
    uwsgi \
    uwsgi-plugin-python \
    nginx \
    supervisor \
    curl \
  && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN sudo apt-get install -y nodejs

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY requirements.txt /home/facelook/
RUN pip install -r /home/facelook/requirements.txt

COPY app /home/facelook/app

COPY client/package.json /home/facelook/client/
WORKDIR /home/facelook/client
RUN npm i --no-optional
COPY client/. /home/facelook/client
RUN npm run build && rm -rf /home/facelook/client

COPY uwsgi.ini /home/facelook/uwsgi.ini
COPY wsgi.py /home/facelook/wsgi.py

EXPOSE 80
CMD ["/usr/bin/supervisord"]
