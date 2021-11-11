FROM ubuntu:12.10

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update

# Install Java JDK
#   `--no-install-recommends` avoids an issue with `fuse` but is not needed in
#   docker 0.10.0 (but Amazon EB has 0.9.0)
#   See: https://github.com/dotcloud/docker/issues/963
RUN apt-get install -y --no-install-recommends openjdk-7-jdk

# Install Python-related dependencies
RUN apt-get install -y libevent-dev python-all-dev python-setuptools

# Install pip
RUN easy_install pip

# Install packages
RUN pip install Flask==0.10.1 Flask-Sockets==0.1 GitPython==0.3.2.RC1 Jinja2==2.7.2 MarkupSafe==0.21 Werkzeug==0.9.4 argparse==1.2.1 async==0.6.1 distribute==0.6.24 gevent==1.0.1 gevent-websocket==0.9.3 gitdb==0.5.4 greenlet==0.4.2 gunicorn==18.0 itsdangerous==0.24 smmap==0.8.2 wsgiref==0.1.2
