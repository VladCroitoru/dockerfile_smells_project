FROM python:3.6

WORKDIR /usr/src/
COPY requirements.txt  /usr/src/requirements.txt
RUN pip install -r requirements.txt

COPY ethermine_exporter.py  /usr/src/ethermine_exporter.py

EXPOSE      9118
ENTRYPOINT  [ "python", "/usr/src/ethermine_exporter.py" ]
