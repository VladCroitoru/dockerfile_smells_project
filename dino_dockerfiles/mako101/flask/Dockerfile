FROM ubuntu

RUN apt-get install -y python-setuptools

RUN easy_install pip

ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

ADD . /src

EXPOSE 5000


CMD python src/app.py
