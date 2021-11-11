FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3.9
RUN apt-get install -y pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]