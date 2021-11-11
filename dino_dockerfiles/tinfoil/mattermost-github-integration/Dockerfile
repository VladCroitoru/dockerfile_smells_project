FROM python:3-alpine

RUN apk add --no-cache build-base jpeg-dev zlib-dev

# for a flask server
EXPOSE 5000

ENV HOME /app

COPY requirements.txt $HOME/requirements.txt
RUN pip install -r $HOME/requirements.txt

COPY . $HOME
WORKDIR $HOME

CMD ["python", "server.py"]
