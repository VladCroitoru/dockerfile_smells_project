# Use an official Python runtime as a parent image
FROM continuumio/anaconda3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./data/ /app

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt
RUN mkdir ~/.jupyter
RUN mv jupyter_notebook_config.py ~/.jupyter/
# RUN rm /etc/apt/sources.list
# RUN mv sources.list /etc/apt/
# RUN apt-get update && apt-get install -y bzip2 apt-utils
# RUN ./Anaconda3-5.0.0-Linux-ppc64le.sh -b
#RUN ["bash","./Anaconda3-5.0.0-Linux-ppc64le.sh"]

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
# ENV NAME World

# Run app.py when the container launches

CMD [ "jupyter-notebook" ,"--allow-root"]