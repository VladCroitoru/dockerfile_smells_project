FROM klakegg/hugo:ubuntu as builder

RUN apt-get update -y

RUN apt-get install -y git

WORKDIR /src

COPY . /src

ENV HUGO_ENV=production

RUN git submodule update --init --recursive && hugo version && hugo --minify


FROM nginx

COPY --from=builder /src/public /app

COPY conf/nginx.conf /etc/nginx/conf.d/default.conf
