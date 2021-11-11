FROM nginx

RUN apt-get update && apt-get install -y \
  nano

RUN mkdir /etc/nginx/sites-available
RUN mkdir /etc/nginx/sites-enabled


COPY nginx.conf /etc/nginx/nginx.conf

COPY sites-available/step-1 /etc/nginx/sites-available/step-1
COPY sites-available/step-2 /etc/nginx/sites-available/step-2

RUN ln -s /etc/nginx/sites-available/step-1 /etc/nginx/sites-enabled/step-1
RUN ln -s /etc/nginx/sites-available/step-2 /etc/nginx/sites-enabled/step-2
