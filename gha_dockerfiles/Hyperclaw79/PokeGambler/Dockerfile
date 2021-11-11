FROM python:3.9.6-slim
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/bot
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "launcher.py" ]