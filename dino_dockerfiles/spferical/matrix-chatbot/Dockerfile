from python:3-alpine

env MATRIX_CHATBOT_CONFIG "/matrixbot/data/config.cfg"
env MATRIX_CHATBOT_BRAIN "/matrixbot/data/brain.db"

run apk add --no-cache git

run adduser -S matrixbot

workdir /matrixbot

volume /matrixbot/data/

copy requirements.txt /matrixbot/

run pip install -r requirements.txt

copy ./*.py docker_entrypoint.sh /matrixbot/

cmd [ "sh", "docker_entrypoint.sh" ]
