FROM python:3.9-buster

# Prepare app dir
RUN mkdir /app
WORKDIR /app
RUN mkdir ./run ./log

# Prepare virtualenv
RUN python3 -m venv ./virtualenv
RUN ./virtualenv/bin/pip install --upgrade pip setuptools

# Install dependencies
COPY ./requirements.txt .
RUN ./virtualenv/bin/pip install -r requirements.txt

# Install application
COPY README.md setup.py ./
COPY bin/ ./bin
COPY fakesmtpd/ ./fakesmtpd
RUN ./virtualenv/bin/pip install .

# Start eventstreamd
EXPOSE 25
COPY start.sh ./
CMD ["/app/start.sh"]
