FROM python:3
MAINTAINER Peter Georgeson "peter@supernifty.org"
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
