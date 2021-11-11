FROM python:3-alpine AS devoxxfr_amadeus_api

ENV FLASK_APP=/api/api.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=8080 \
    WERKZEUG_RUN_MAIN=true \
    MANIFEST_FILE_PATH=/manifest.json

COPY api /api
COPY manifest.json /

WORKDIR /api

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python3", "-m", "flask", "run"]

FROM php:7.4-fpm AS devoxxfr_amadeus_ui_fpm

ARG user
ARG uid
ARG home

COPY ./ui /var/www
COPY ./manifest.json /

RUN mkdir -p $home/$user && \
    useradd -G www-data,root -u $uid -d $home/$user $user && \
    chown -R $user:$user $home/$user

WORKDIR /var/www

USER $user

FROM nginx:alpine AS devoxxfr_amadeus_ui_nginx

COPY --from=devoxxfr_amadeus_ui_fpm /manifest.json /manifest.json
COPY --from=devoxxfr_amadeus_ui_fpm /var/www /var/www

COPY ./.docker/nginx/ui.conf /etc/nginx/conf.d/default.conf

WORKDIR /var/www

USER $user
