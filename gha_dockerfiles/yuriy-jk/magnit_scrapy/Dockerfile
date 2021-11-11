FROM python:3.9

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD scrapy crawl magnit -O items.json


# docker run -v $(pwd):/code mag