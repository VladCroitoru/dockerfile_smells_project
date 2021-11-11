FROM python:3

ENV PYTHONUNBUFFERED=1
ENV HOME /root

RUN apt-get update

WORKDIR /root

RUN apt-get update --fix-missing
RUN apt-get install -y nodejs
RUN apt-get install -y npm

COPY . .

RUN npm install --prefix ./zeal_frontend
RUN npm rebuild node-sass --prefix ./zeal_frontend

RUN npm --prefix ./zeal_frontend run build

RUN pip install -r ./zeal_backend/requirements.txt

CMD python ./zeal_backend/manage.py makemigrations && python ./zeal_backend/manage.py migrate && python ./zeal_backend/manage.py runserver 0:$PORT