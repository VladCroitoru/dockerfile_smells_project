FROM ubuntu:xenial

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3-virtualenv git
RUN git clone https://github.com/Psycojoker/t2m /srv
WORKDIR /srv
RUN git reset --hard 53f6a603e3f7df3faab20ff5ee6eb5dbe2e068c7
RUN python3 -m virtualenv --python=python3 ve
RUN bash -c 'source ve/bin/activate && pip install -r requirements.txt'
ADD run.sh setup.sh /srv/
RUN chmod a+x run.sh setup.sh
CMD ["bash", "/srv/run.sh"]