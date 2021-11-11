FROM python:3.8-slim

RUN apt-get update && apt-get install -y python3-pip
ADD ./webapp/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

# $PORT is set by Heroku

# DEVELOPMENT
# FROM base as dev
# herokuはvolumeサポートしてない
# WORKDIR /webapp
# Flask
# CMD gunicorn --bind 0.0.0.0:$PORT wsgi
# FastAPI
# main部分が最初に実行されるファイル名
# (TODO) {$PORT}と書いたら変数は渡ってるけどuvicornが起動できない(数字直書きだと動く)
# []外したら動く
# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000", "--log-level", "trace", "--use-colors"]
# CMD uvicorn main:app --reload --host 0.0.0.0 --port $PORT --log-level trace --use-colors

# PRODUCTION
# FROM base as prod
ADD ./ /webapp/
WORKDIR /webapp
CMD uvicorn webapp.main:app --host 0.0.0.0 --port $PORT --log-level trace --use-colors