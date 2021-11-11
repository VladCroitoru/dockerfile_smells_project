FROM python:3.9.7-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt --timeout=60
COPY covid19_dash covid19_dash
CMD ["waitress-serve", "covid19_dash:server"]
