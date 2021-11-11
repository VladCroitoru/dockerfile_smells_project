from ubuntu:14.04.1

maintainer Dockerfiles
RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse' > /etc/apt/sources.list
RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse' >> /etc/apt/sources.list
RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse' >> /etc/apt/sources.list
RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse' >> /etc/apt/sources.list
RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse' >> /etc/apt/sources.list
RUN echo 'deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse' >> /etc/apt/sources.list
RUN echo 'deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse' >> /etc/apt/sources.list
RUN echo 'deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse' >> /etc/apt/sources.list
RUN echo 'deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse' >> /etc/apt/sources.list
RUN echo 'deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse' >> /etc/apt/sources.list
run apt-get update
run apt-get install -y build-essential git
run apt-get install -y python python-dev python-setuptools
run apt-get install -y nginx supervisor
run easy_install pip

# install uwsgi now because it takes a little while
run pip install uwsgi

# install nginx
run apt-get install -y python-software-properties
run apt-get update
run apt-get install -y sqlite3

# install our code
add . /home/docker/code/

# setup all the configfiles
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /home/docker/code/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /home/docker/code/supervisor-app.conf /etc/supervisor/conf.d/

# run pip install
run pip install -r /home/docker/code/requirements.txt

# install django, normally you would remove this step because your project would already
# be installed in the code/app/ directory
run django-admin.py startproject website /home/docker/code/

expose 80
cmd ["supervisord", "-n"]
