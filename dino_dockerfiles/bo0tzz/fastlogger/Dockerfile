FROM node:alpine as assets

RUN apk add --no-cache git

WORKDIR /usr/src/app

COPY package.json /usr/src/app/package.json
COPY yarn.lock /usr/src/app/yarn.lock

RUN yarn install


FROM python:3-alpine

EXPOSE 8080

WORKDIR /usr/src/app

RUN apk add --no-cache git tzdata

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY --from=assets /usr/src/app/node_modules/bootstrap/dist/css/bootstrap.min.css /usr/src/app/node_modules/bootstrap/dist/css/bootstrap.min.css
COPY --from=assets /usr/src/app/node_modules/jquery/dist/jquery.min.js /usr/src/app/node_modules/jquery/dist/jquery.min.js
COPY --from=assets /usr/src/app/node_modules/popper.js/dist/popper.min.js /usr/src/app/node_modules/popper.js/dist/popper.min.js
COPY --from=assets /usr/src/app/node_modules/bootstrap/dist/js/bootstrap.min.js /usr/src/app/node_modules/bootstrap/dist/js/bootstrap.min.js
COPY --from=assets /usr/src/app/node_modules/plotly.js/dist/plotly.min.js /usr/src/app/node_modules/plotly.js/dist/plotly.min.js

COPY static/index.html /usr/src/app/static/index.html
COPY static/style.css /usr/src/app/static/style.css
COPY static/js.js /usr/src/app/static/js.js
COPY static/octocat.png /usr/src/app/static/octocat.png

COPY main.py /usr/src/app/main.py

CMD ["python", "-u", "./main.py"]
