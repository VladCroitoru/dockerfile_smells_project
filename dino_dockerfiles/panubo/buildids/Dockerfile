FROM python:2.7

ENV STORAGE_PATH=/data
EXPOSE 8080

ADD requirements.txt /usr/src/
RUN pip install -r /usr/src/requirements.txt
ADD *.py /usr/src/

CMD ["/usr/src/entry.py", "/usr/src/app.py", "8080"]
