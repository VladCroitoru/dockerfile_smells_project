from python:3.9-slim-buster

# Install requirements
COPY requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt 

# Copy code, models, config
COPY . /home
COPY dev_config.json /home/config.json
COPY cis/test.db /home/favorites.db
ADD https://cacerts.digicert.com/DigiCertSHA2SecureServerCA.crt.pem /home/digicert.pem
RUN cat /home/digicert.pem >> $(python -m certifi)
WORKDIR /home

# Run server
ENTRYPOINT python wsgi.py --model_path /home/models/distilbert-12-10 --label_mapping_path /home/models/label_mapping.json --config_path /home/config.json --database_uri sqlite:////home/favorites.db