FROM ubuntu

RUN apt-get update
RUN apt-get install -y python python-pip libpython-dev
ADD . /app/
RUN pip install -r /app/requirements.txt

CMD /usr/bin/python /app/docker-dns.py