FROM python:3.8-alpine

LABEL authors="Konstantin Goretzki, Felix Alexa"
LABEL version="v1.2"
LABEL description="This image contains a gunicorn server with our RSS/ Atom reader Freedy installed."

# uses https://github.com/konstantingoretzki/freedy
ARG FREEDY_VERSION=v1.0.0
ARG FREEDY_DOWNLOAD_SHA512=53e27a567ee251d55389d95018f9a700f9648934a6f3d2a81e53afdea7feb31796f2a188c36ca36488049612d18410d9f194ac3084bf73c6e964317aae428973

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
