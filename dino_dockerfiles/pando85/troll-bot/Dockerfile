FROM python:3.5

ADD . /troll-bot
WORKDIR /troll-bot
RUN pip install -r requirements.txt

# espeak and oggenc
RUN apt-get update && apt-get install -y espeak vorbis-tools

CMD ["python", "-m", "troll_bot"]
