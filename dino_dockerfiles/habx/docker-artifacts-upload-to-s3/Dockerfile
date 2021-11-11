FROM debian

RUN apt-get update && apt-get install -y python python-pip curl unzip groff
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install awscli

COPY entrypoint.sh /bin/

CMD ["/bin/entrypoint.sh"]
