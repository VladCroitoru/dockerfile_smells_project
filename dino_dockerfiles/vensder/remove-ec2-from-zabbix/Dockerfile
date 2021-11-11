FROM python:3.6.3-jessie

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY boto.cfg /etc/boto.cfg
CMD ./run_with_sleep.sh
