FROM python:alpine
MAINTAINER Tomasz Kapalka "tomasz.kapalka@amartus.com"
RUN pip install Flask
ENV ENV_VARIABLE Test2
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["main.py"]
