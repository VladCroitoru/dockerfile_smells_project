FROM nikolaik/python-nodejs:python3.9-nodejs14

WORKDIR /var/www/app

# install dep
RUN apt-get update && apt-get install iproute2 nginx -y

COPY . /var/www/app

# backend
WORKDIR /var/www/app/backend
RUN mkdir .venv
RUN pipenv install --deploy
RUN sed -i "s/YYYY-MM-DD/`git log -1 --format="%at" | xargs -I{} date -d @{} +%Y-%m-%d`/g" version.py
RUN sed -i "s/development/`git rev-parse HEAD`/g" version.py

# frontend
WORKDIR /var/www/app/frontend
RUN npm install
RUN export REACT_APP_BACKEND_URL="" && npm run build

# proxy
RUN echo "server_tokens off;" >> /etc/nginx/conf.d/server_tokens.conf

WORKDIR /var/www/app
RUN cp /var/www/app/nginx.conf /etc/nginx/sites-enabled/default

EXPOSE 80
CMD [ "/var/www/app/entrypoint.sh" ]
