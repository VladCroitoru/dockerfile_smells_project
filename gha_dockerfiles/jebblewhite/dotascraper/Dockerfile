FROM python:3.8-slim-buster

COPY . .

RUN apt-get -y update &&\
    apt install -y wget &&\
    apt install -y gnupg &&\ 
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - &&\
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' &&\
    apt-get -y update &&\
    apt-get install -y google-chrome-stable &&\
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip &&\
    apt-get install -yqq unzip &&\
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ &&\
    pip install dotascraper==0.0.4


ENV DISPLAY=:99

CMD [ "python", "-m" , "dotaproscraper" ]