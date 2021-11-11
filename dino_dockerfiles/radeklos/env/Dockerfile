FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
ENV FLASK_APP=app.py
COPY . /app
WORKDIR /app
RUN pip install flask
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
