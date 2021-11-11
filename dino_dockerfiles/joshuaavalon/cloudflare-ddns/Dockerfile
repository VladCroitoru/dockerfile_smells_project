FROM python:alpine

WORKDIR /ddns
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY crontab .
RUN crontab crontab
COPY cloudflare_ddns ./cloudflare_ddns
COPY run.py .

CMD python run.py && crond -f
