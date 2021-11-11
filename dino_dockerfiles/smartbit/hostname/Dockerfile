FROM ubuntu:xenial

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get clean all

RUN pip install flask

ADD hello.py /tmp/hello.py

CMD ["python","/tmp/hello.py"]
