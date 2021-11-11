FROM python:3.9-alpine

LABEL authors="Konstantin Goretzki, Felix Alexa"
LABEL version="v1.3"
LABEL description="This image contains a gunicorn server with our RSS / Atom reader Freedy installed."

# uses https://github.com/konstantingoretzki/freedy
ARG FREEDY_VERSION=v1.0.1
ARG FREEDY_DOWNLOAD_SHA512=1e3fa4319edf9c9440f68335cc09fd933f322e10b59a2095c7d371b66be105aa43f3dc4b6aea96b8480a6aca887be240a2967e43a6db02508c300d5df4e74282

RUN adduser -D freedy

WORKDIR /home/freedy
COPY boot.sh ./

RUN apk update \
    && apk add --no-cache curl \
    && curl -fSL -o freedy.tar.gz "https://github.com/konstantingoretzki/freedy/archive/$FREEDY_VERSION.tar.gz" \
    && echo "$FREEDY_DOWNLOAD_SHA512  freedy.tar.gz" | sha512sum -c \
    && tar -xf freedy.tar.gz --strip-components=1 \
    && rm freedy.tar.gz

RUN python -m venv venv \
    && venv/bin/pip install --no-cache-dir -r requirements.txt \
    && venv/bin/pip install --no-cache-dir gunicorn \
    && chmod +x boot.sh 
    
ENV FLASK_APP freedy.py

RUN chown -R freedy:freedy ./
USER freedy

EXPOSE 5000
VOLUME /home/freedy/config
CMD [ "./boot.sh" ]
