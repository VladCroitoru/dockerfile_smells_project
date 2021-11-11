# Set python:3 as Base image
FROM python:3

# Set the working directory for RUN, CMD, ENTRYPOINT, COPY and ADD
WORKDIR /usr/src/app

# Copy requirements.txt to a path relative to WORKDIR
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy the other files to a path relative to WORKDIR
COPY . .

# Run the following commands
ENV AIRFLOW_HOME=/usr/src/app
RUN airflow initdb
RUN python remove_airflow_examples.py
RUN airflow resetdb -y
RUN python customize_dashboard.py

# Set command to run as soon as container is up
CMD airflow webserver -p=$PORT
