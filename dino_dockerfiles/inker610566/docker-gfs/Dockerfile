FROM python:2.7
RUN pip install --upgrade google-api-python-client
RUN apt-get update \
    && apt-get install -y git \
    && apt-get autoclean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /root
RUN git clone https://github.com/inker610566/gfs && mv gfs/gfs /usr/local/lib/python2.7/site-packages/ && rm -r *
COPY backup /bin
RUN chmod +x /bin/backup
