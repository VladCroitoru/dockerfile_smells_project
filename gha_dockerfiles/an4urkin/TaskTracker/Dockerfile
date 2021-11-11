FROM python:3.9.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for project in the container
RUN mkdir /var/task_Track

# Set the working directory to /task_Track
WORKDIR /var/task_Track

# Copy the current directory contents into the container at /task_Track
ADD . /var/task_Track/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
