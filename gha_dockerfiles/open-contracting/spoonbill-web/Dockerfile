FROM python:3.7-alpine
ENV PYTHONDONTWRITEBYTECODE 1

ARG USER=spoonbill
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

RUN apk update && apk add libpq sudo --no-cache && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev libffi-dev rust cargo g++ gettext git \
        && adduser -D $USER \
        && echo "$USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$USER \
        && chmod 0440 /etc/sudoers.d/$USER \
        && pip install --no-cache-dir -r requirements.txt \
        && ./manage.py compilemessages \
        && apk del .build-deps gcc python3-dev musl-dev postgresql-dev libffi-dev rust cargo g++ gettext git \
        && rm -fr /root/.cache \
        && rm -fr /usr/src/app/src/standard-theme \
        && rm -fr /root/.cargo
RUN chown -R $USER:$USER /usr/src/app

EXPOSE 8000

USER spoonbill
CMD ["gunicorn", "spoonbill_web.wsgi", "0:8000"]
