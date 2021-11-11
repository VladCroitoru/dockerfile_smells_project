FROM python:3.8

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py /app.py
COPY entry.sh /entry.sh

EXPOSE 5000

CMD [ "bash", "entry.sh" ]