FROM python:3.9-alpine
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY update-dns.py /update-dns.py
ENV PYTHONUNBUFFERED 1
RUN chmod a+x /update-dns.py
CMD [ "/update-dns.py" ]