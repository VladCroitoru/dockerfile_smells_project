FROM python:3.5.2-alpine

MAINTAINER Kevin Li <mlf4aiur@gmail.com>

WORKDIR /myapp

COPY weather.py test_weather.py /myapp/
COPY fixtures/ /myapp/fixtures/

RUN pip install Flask==0.11.1

ENV PORT 5000
ENV APP_ID YOUR_APP_ID
ENV TEMP_SCALE C
ENV LOG_LEVEL INFO

EXPOSE 5000

CMD ["/myapp/weather.py"]
