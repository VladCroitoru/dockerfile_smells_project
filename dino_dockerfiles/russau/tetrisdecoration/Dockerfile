FROM ubuntu:12.04
MAINTAINER russ <russell.sayers@gmail.com>

RUN apt-get -y update && apt-get install -y python-pip gcc python-dev
RUN pip install --upgrade pip

# Setup Flask-SocketIO application
COPY app /TetrisDecoration
RUN /usr/local/bin/pip install -r /TetrisDecoration/requirements.txt

# Start processes
EXPOSE 5000
CMD ["python", "/TetrisDecoration/app.py"]
