FROM python:3.9.6-alpine

RUN mkdir "/srv/urlman"
RUN pip install pipenv

WORKDIR /srv/urlman

COPY . /srv/urlman/

RUN pipenv install

ENV FLASK_APP=/srv/urlman/urlman
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0
ENV DATABASE=/srv/urlman/db.sqlite

CMD ["pipenv", "run", "flask", "run"]