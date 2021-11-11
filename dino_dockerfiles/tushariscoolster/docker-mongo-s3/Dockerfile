FROM mongo
MAINTAINER Tushar Borole <tusharborole@ymail.com>
RUN mkdir /script
ADD . /script
RUN  apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y  python-pip groff-base cron
RUN rm -rf /var/lib/apt/lists/*
RUN pip install awscli
ADD start.sh /start.sh
RUN chmod +x /start.sh
CMD /start.sh
