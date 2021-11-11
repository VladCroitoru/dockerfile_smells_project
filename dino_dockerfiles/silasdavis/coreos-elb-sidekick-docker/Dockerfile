from ubuntu:14.10

RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install python-daemon
RUN pip install elb-dance
ADD boto.cfg /etc/boto.cfg
ADD elb-daemon.py /usr/local/bin/elb-daemon
RUN chmod +x /usr/local/bin/elb-daemon
ENTRYPOINT ["elb-daemon"]
