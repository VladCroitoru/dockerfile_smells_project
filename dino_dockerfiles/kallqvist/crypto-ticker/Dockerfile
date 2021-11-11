FROM ubuntu
MAINTAINER kallqvist@gmail.com
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y python python-pip
RUN pip2 install https://download.electrum.org/2.9.3/Electrum-2.9.3.tar.gz
ADD ./code/setup.py /build/setup.py
ADD ./code/requirements.txt /build/requirements.txt
RUN pip install --upgrade pip /build && rm -R /build
ADD ./code /code
ADD docker-entrypoint.sh /docker-entrypoint.sh
WORKDIR /code
EXPOSE 5000
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["python", "run.py"]
