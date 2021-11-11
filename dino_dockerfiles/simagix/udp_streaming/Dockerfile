FROM ubuntu

RUN apt-get update
RUN apt-get -y install wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN apt-get -y install python
RUN python get-pip.py
RUN pip install Flask

EXPOSE 5000
ADD . /usr/src/app
WORKDIR /usr/src/app
CMD ["/usr/src/app/server.py", "/etc/library.repo"]

