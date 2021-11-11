FROM tensorflow/tensorflow:2.5.1-gpu

ENV DEBIAN_FRONTEND=noninteractive

# Apt-get installs
RUN apt-get update && apt-get install -y tree vim && apt-get install ffmpeg libsm6 libxext6  -y

# Install all the requirements
COPY requirements.txt /tmp
RUN python3 -m pip install --upgrade pip && cd /tmp && python3 -m pip install -r requirements.txt --user

# Copy model
COPY models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5 /root/.keras/models/

# Copy the project
COPY deeplab/ /home/deeplab
COPY *.py /home/
COPY *.sh /home/

# create output directory
RUN mkdir -p "/home/output"

# Expose ports - tensorboard
EXPOSE 6006

# Set working directory
WORKDIR /home

# Startup command
#CMD ["python3", "server.py"]

