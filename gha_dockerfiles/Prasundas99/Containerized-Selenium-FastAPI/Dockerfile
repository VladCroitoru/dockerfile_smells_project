FROM python:3.9-slim

# Installing depedencies in ubuntu to install google chrome
RUN apt-get update \
    && apt-get install -y \
        fonts-liberation \
        libasound2 \
        libatk-bridge2.0-0 \
        libatk1.0-0 \
        libatspi2.0-0 \
        libcups2 \
        libdbus-1-3 \
        libdrm2 \
        libgbm1 \
        libgtk-3-0 \
        libnspr4 \
        libnss3 \
        libx11-xcb1 \
        libxcb-dri3-0 \
        libxcomposite1 \
        libxdamage1 \
        libxfixes3 \
        libxrandr2 \
        xdg-utils \
        libcurl3-gnutls \
        libcurl3-nss \
        libcurl4 \
        wget

COPY ./ /app/
COPY ./requirements.txt /app
# latest version of google chrome
COPY ./applications/google-chrome-stable_current_amd64.deb /app/applications/

WORKDIR /app 

RUN pip3 install -r requirements.txt
RUN dpkg -i applications/google-chrome-stable_current_amd64.deb


EXPOSE 8080

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
