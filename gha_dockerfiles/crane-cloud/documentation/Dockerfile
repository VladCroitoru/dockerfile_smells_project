FROM python:3.6 as build

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY cranecloud /app

RUN mkdocs build

FROM nginx

COPY --from=build /app/site /usr/share/nginx/html

