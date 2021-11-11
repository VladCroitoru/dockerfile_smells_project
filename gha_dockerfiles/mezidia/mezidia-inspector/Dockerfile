FROM python:slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "-m", "inspector" ]
