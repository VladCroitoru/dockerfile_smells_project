FROM python:3.5.2-alpine

MAINTAINER Kevin Li <mlf4aiur@gmail.com>

RUN mkdir -p /myapp
WORKDIR /myapp

COPY stock_price.py test_stock_price.py /myapp/
COPY fixtures/ /myapp/fixtures/

RUN pip install Flask==0.11.1

ENV PORT 5000

EXPOSE 5000

CMD ["/myapp/stock_price.py"]
