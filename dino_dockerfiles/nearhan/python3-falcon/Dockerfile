FROM python:3.4.3

ADD requirements.txt /code/requirements.txt
ADD main.py /code/main.py
RUN pip install -r /code/requirements.txt

EXPOSE 5000

ADD run /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

WORKDIR /code/

CMD ["/usr/local/bin/run"]
