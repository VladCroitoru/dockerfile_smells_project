FROM python:latest

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create working dir
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# Expose the port
EXPOSE 5000