FROM python:3.6-alpine3.7

WORKDIR /app

COPY *requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD [ "python3", "httpenv.py" ]
EXPOSE 80
ENV PYTHONUNBUFFERED=1
LABEL name=httpenv version=dev
