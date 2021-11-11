FROM python:3.8

WORKDIR /my_app

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip && pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile
RUN pipenv install

#CMD ["/bin/bash", "run.sh"]
