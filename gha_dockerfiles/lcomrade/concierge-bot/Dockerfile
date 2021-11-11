# BUILD
FROM python:3-alpine as build

WORKDIR /build

RUN apk update && apk upgrade && apk add --no-cache gcc libc-dev

COPY requirements.txt ./

RUN pip install --user --no-cache-dir -r requirements.txt


# RUN
FROM python:3-alpine as run

WORKDIR /bot

COPY --from=build /root/.local /root/.local

COPY . .

RUN chmod +x /bot/*.sh

VOLUME /bot/data

CMD [ "python", "./main.py" ]
