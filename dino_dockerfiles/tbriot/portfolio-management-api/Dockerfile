FROM python:3

WORKDIR /usr/src/portfolio-management-api

RUN pip install flask
COPY . .

CMD [ "python", "./pyfolio/rest_api.py", "-DFOREGROUND" ]
