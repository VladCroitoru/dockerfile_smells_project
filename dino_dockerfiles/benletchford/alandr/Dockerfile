FROM python:2

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r server/requirements.txt

RUN apt-get update -y && \
  apt-get install npm -y && \
  npm install -g n && n stable && \
  npm install yarn -g

RUN cd www && yarn install && yarn build

CMD [ "python", "./server/alandr.py", "--data-directory=/data", "--host=0.0.0.0", "--port=80" ]
