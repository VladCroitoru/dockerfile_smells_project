FROM python:latest
WORKDIR .
COPY . .
RUN pip3 install --upgrade pip setuptools
RUN pip3 install --no-cache-dir -r requirements.txt
CMD python3 main.py
