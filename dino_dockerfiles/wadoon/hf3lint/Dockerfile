FROM wadoon/flaskapp


MAINTAINER Alexander Weigl <Alexander.Weigl@student.kit.edu>

RUN sudo apt-get -y install libxml2-dev libxslt1-dev python-dev libz-dev

ENV PYTHONPATH /app

ADD . /app

WORKDIR /app
RUN sudo pip install -r requirements.txt
RUN sudo pip install -r requirements-web.txt

ADD gunicornconfig.py /etc/gunicornconfig.py

ENTRYPOINT gunicorn -c /etc/gunicornconfig.py hf3lint.web:app