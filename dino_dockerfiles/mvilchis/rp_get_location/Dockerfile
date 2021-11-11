FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev  vim \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN mkdir webhook

ADD . webhook/

WORKDIR webhook

RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD ["./start.sh"]
