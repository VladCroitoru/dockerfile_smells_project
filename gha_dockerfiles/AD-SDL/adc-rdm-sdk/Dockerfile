FROM python:3 as build

WORKDIR /app
COPY . ./

RUN pip install mkdocs mkdocs-material mkdocs-typer mkdocstrings
RUN pip install .
RUN mkdocs build

FROM nginx:alpine

RUN mkdir -p /var/www/html/client
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/site/ /usr/share/nginx/html/docs/sdk
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]