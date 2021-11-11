FROM python:3.4

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
CMD ["python", "hubhook.py"]
EXPOSE 8800
