FROM python:3.6

RUN mkdir -p /usr/src/app
COPY . /usr/src/app/
WORKDIR /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

ARG TG_CALENDAR_BOT_TOKEN
ENV TG_CALENDAR_BOT_TOKEN=$TG_CALENDAR_BOT_TOKEN

ENV PORT 80

CMD cd bot_calendario_telegram/ && python reminder_rest_api.py
# CMD cd bot_calendario_telegram/ && python bot.py

EXPOSE 80
