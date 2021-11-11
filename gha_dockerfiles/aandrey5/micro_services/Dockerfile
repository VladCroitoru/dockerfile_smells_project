# start main
FROM python:3.8

WORKDIR /usr/src/app

# install requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy application
COPY app.py app.py

# run command
CMD [ "python", "./app.py" ] 

EXPOSE 8090 443
