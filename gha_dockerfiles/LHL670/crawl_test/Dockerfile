FROM python:3.8.10

WORKDIR /cgu_crawl

ADD . /cgu_crawl

RUN pip install -r requirements.txt

EXPOSE 8888 9050 9051


CMD [ "python3", "cgu_crawl/CGUScholar_personalPage.py" ]