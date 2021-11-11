FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

# for adding chrome and its driver for scraping
# install system dependencies
RUN apt-get -y install gcc make \
    && apt-get install -y wget \
    && apt-get install -y curl \
    && apt-get install -y gnupg2 \
    && rm -rf /var/lib/apt/lists/*s
# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# COPY ./django_project /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

