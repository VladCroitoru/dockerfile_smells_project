FROM python:2.7.13
RUN pip install galaxy-parsec==1.0.2 && apt-get update && apt-get install -y jq && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
