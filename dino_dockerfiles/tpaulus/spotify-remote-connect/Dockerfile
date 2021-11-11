FROM python:3
MAINTAINER Tom Paulus "tom@tompaulus.com"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "./SpotifyConnect.py" ]
