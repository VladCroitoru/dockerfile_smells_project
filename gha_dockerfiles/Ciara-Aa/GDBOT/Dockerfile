FROM python:latest
WORKDIR /root/bot
COPY . .
RUN pip3 install --upgrade pip setuptools
RUN pip install -U -r requirements.txt
# Starting Worker
CMD ["python3","-m","bot"]
