FROM python:3-slim

# Additional dependencies required to support Snappy compression, mmh3:
RUN apt-get update && apt-get install -y --no-install-recommends \
        libsnappy-dev \
        g++ \
        git \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD gunicorn --workers 20 --timeout 6000 --error-logfile - --access-logfile - --bind 0.0.0.0:8000 logs:app


