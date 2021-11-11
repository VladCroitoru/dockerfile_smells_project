FROM ubuntu
RUN apt-get update \
    && apt-get install -y wget python3 curl \
    && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" \
    && apt-get remove --purge -y curl \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/*
RUN python3 get-pip.py
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["python3", "-u", "laundromat.py"]