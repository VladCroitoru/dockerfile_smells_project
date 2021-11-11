FROM ubuntu:trusty

RUN apt-get update
RUN apt-get -y install software-properties-common python-software-properties
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update
RUN apt-get install -y git python python-dev python-setuptools supervisor nginx sqlite3 
RUN apt-get install -y curl apache2-utils siege iperf
RUN easy_install pip

# install uwsgi now because it takes a little while
RUN pip install uwsgi

# install our code
ADD . /home/docker/code/
RUN pip install -r /home/docker/code/app/requirements.txt

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /home/docker/code/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s /home/docker/code/supervisor-app.conf /etc/supervisor/conf.d/

EXPOSE 80
EXPOSE 5201
cmd ["supervisord", "-n"]
