FROM alpine

RUN apk update
RUN apk add python3 nodejs nodejs-npm
RUN python3 -m ensurepip

ADD achievements.py authentication.py coffee.py config.py database.py \
    package.json package-lock.json Pipfile Pipfile.lock \
    webpack.config.js .babelrc /coffee/
ADD templates /coffee/templates
ADD static /coffee/static

WORKDIR coffee

RUN pip3 install pipenv
RUN pipenv install
RUN npm install && npm run build

EXPOSE 5000

ENV DB_HOST=mongo
ENV FLASK_APP=coffee.py

CMD pipenv run flask run --host 0.0.0.0
