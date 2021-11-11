FROM python:2
EXPOSE 8000

RUN groupadd -r djbot && useradd -u 1000 --no-log-init -r -m -g djbot djbot

RUN apt-get update -qq && apt-get install -yqq \
    sshpass \
 && rm -rf /var/lib/apt/lists/*

COPY pytest.ini setup.py setup.cfg gunicorn.py /home/djbot/app/
COPY src /home/djbot/app/src
WORKDIR /home/djbot/app

RUN chown -R djbot /home/djbot/app

RUN pip install -e .
# python setup.py install

USER djbot

#Logs
RUN mkdir -p /home/djbot/log
ENV LOGS '/home/djbot/log'
VOLUME /home/djbot/log

#SSH
RUN mkdir -p /home/djbot/.ssh && touch /home/djbot/.ssh/.none

# Install application and requirements
VOLUME /home/djbot/app

CMD ["gunicorn", "--forwarded-allow-ips=*", "--config=gunicorn.py", "wsgi:app"]
