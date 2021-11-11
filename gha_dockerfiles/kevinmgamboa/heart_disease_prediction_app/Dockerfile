# Defining Docker Image
FROM python:3.8
# Defining pretent working directorty
WORKDIR /heart_disease_prediction_app
# Copy repo content into working dir
ADD . /heart_disease_prediction_app
# Installing dependencies (requirements.txt)
RUN pip install -r app_requirements.txt
# Define commands when starting container
CMD ["python", "app.py"]