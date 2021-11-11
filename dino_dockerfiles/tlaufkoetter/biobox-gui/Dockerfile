FROM debian:8

MAINTAINER Tobias Laufkötter <tlaufkoetter@techfak.uni-bielefeld.de>

RUN apt-get -y update && apt-get -y install python3 curl
RUN curl https://bootstrap.pypa.io/get-pip.py | python3

# import the bioboxgui's files into the container.
ENV PROJECT_ROOT /opt/application
COPY requirements.txt $PROJECT_ROOT/requirements.txt
COPY run.py $PROJECT_ROOT/run.py
COPY config.py $PROJECT_ROOT/config.py
COPY bioboxgui $PROJECT_ROOT/bioboxgui

RUN mkdir $PROJECT_ROOT/db
RUN pip install -r $PROJECT_ROOT/requirements.txt

EXPOSE 5000

ENTRYPOINT cd $PROJECT_ROOT && python3 run.py --docker
