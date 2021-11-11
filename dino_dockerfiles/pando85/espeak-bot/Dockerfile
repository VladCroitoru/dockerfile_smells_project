FROM python:3.5

ADD . /espeak-bot
WORKDIR /espeak-bot
RUN pip install -r requirements.txt

# espeak and oggenc
RUN apt-get update && apt-get install -y espeak vorbis-tools

CMD ["python", "-m", "espeak_bot"]
