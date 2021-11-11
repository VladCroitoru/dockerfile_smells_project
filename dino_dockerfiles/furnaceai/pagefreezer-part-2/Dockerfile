FROM python:2

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip2 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py -l 10 -s" ]
