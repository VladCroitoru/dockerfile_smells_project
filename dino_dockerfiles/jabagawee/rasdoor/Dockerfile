FROM python:3-alpine

ADD . /rasdoor
WORKDIR /rasdoor

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn && \
    apk add --update openssh-client

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--access-logfile", "-", "--error-logfile", "-"]
