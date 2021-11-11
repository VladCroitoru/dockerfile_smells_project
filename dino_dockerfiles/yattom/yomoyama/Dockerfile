# yomoyama

FROM debian:wheezy
MAINTAINER yattom <tsutomu.yasui@gmail.com>

RUN apt-get update
RUN apt-get install -y curl python2.7 python2.7-dev git
RUN curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python2.7
RUN pip install paver

ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

ADD pavement.py /app/
ADD production_config.py /app/
ADD yomoyama /app/yomoyama
RUN mkdir -p /data/books

ENV YOMOYAMA_CONFIG /app/production_config.py
ENV YOMOYAMA_DATA_DIR /data
ENV SECRET_KEY secret
ENV CLIENT_ID client_id
ENV CLIENT_SECRET client_secret
EXPOSE 5001

#CMD ['-b', '0.0.0.0:5001', '--log-file', 'app.log', '--log-level', 'debug']
#ENTRYPOINT ["gunicorn", "yomoyama.run:app"]
#CMD ["gunicorn", "yomoyama.run:app", "-b", "0.0.0.0:5001", "--log-file", "app.log", "--log-level", "debug"]
CMD ["gunicorn", "yomoyama.run:app", "-b", "0.0.0.0:5001", "--log-level", "debug"]

