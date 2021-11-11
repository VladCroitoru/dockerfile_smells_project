# Docker is telling the Python image to be used for the application.
FROM python:latest

# Creating the "/usr/src/app" directory.
RUN mkdir -p /usr/src/app

# Working directory is being declared to Docker.
WORKDIR /usr/src/app

# The "requirement.txt" file is being copied to the "/usr/src/app" directory.
COPY requirements.txt /usr/src/app

# Using --no-cache-dir flag in pip install, make sure dowloaded packages by pip don't cached on system.
RUN pip install --no-cache-dir -r requirements.txt

# Files in the "/usr/src/app" directory are copied to the root directory.
COPY . /usr/src/app

# Executable container is defined.
ENTRYPOINT ["python","/blog.py"]
