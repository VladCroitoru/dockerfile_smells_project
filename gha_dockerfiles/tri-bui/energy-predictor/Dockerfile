# Base image
FROM python:3.7

# Package files
ADD packages /opt/energy-predictor

# Package install
RUN pip install -e /opt/energy-predictor/gb_api && pip install -e /opt/energy-predictor/gb_model

# App setup
WORKDIR /opt/energy-predictor/gb_api/gb_api
ENV FLASK_APP=run.py
RUN chmod +x run.sh

# Port
EXPOSE 5000

# Run
CMD ["bash", "./run.sh"] 

