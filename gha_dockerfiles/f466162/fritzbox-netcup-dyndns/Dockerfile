FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m compileall

USER nobody

CMD [ "python", "./fb-nc-dyndns.py" ]
