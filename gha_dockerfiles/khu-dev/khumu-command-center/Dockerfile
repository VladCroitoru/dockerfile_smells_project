FROM python:3.8
RUN apt-get update -y && apt-get install -y default-libmysqlclient-dev python3-dev
WORKDIR /khumu
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV KHUMU_ENVIRONMENT DEV
# for python print log
ENV PYTHONUNBUFFERED 0
# 인포21 연동을 위한 selenium 크롬 드라이버
RUN curl https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip -o chromedriver.zip && unzip chromedriver.zip
# please mount a config file later (like /khumu/config/dev.yaml)
ENTRYPOINT ["gunicorn"]