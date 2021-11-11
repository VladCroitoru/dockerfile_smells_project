FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install plotly --upgrade

COPY . .

EXPOSE 8050

CMD [ "python", "./app.py" ]
