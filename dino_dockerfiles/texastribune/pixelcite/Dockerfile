FROM texastribune/gunicorn
MAINTAINER tech@texastribune.org

# modify gunicorn.supervisor.conf to point to custom wsgi
# https://github.com/texastribune/docks/blob/master/gunicorn/gunicorn.supervisor.conf
RUN sed -i 's/wsgi:application/public_app:app/' /etc/supervisor/conf.d/gunicorn.supervisor.conf

# node required for static files
RUN apt-get install nodejs nodejs-legacy npm -y

ADD . /app/

RUN pip install --quiet -r /app/requirements.txt
RUN npm install --quiet

RUN fab render
