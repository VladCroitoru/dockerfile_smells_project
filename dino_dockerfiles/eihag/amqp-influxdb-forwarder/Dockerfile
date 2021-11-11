FROM python:3

WORKDIR .

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY readIotHubAmqpClient.py ./

CMD [ "python3", "./readIotHubAmqpClient.py" ]