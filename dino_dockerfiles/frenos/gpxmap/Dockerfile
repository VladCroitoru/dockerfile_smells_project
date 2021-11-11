FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

VOLUME /usr/src/app/db /usr/src/app/djangomedia

ENTRYPOINT ["/bin/bash", "start.sh"]