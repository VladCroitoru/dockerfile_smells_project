# FROM python:3.6-stretch
FROM python:3.8-slim


# install build utilities
RUN apt-get update && \
	apt-get install -y gcc make apt-transport-https ca-certificates build-essential


# check our python environment
RUN python3 --version
RUN pip3 --version

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y



# set the working directory for containers
WORKDIR  /usr/src/app-name
# WORKDIR /home/ubuntu/app-name
# WORKDIR C:/Users/User/Desktop/Noria/StudyingDocker/app-name3
# https://docs.docker.com/engine/reference/builder/#workdir

# Installing python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all the files from the project’s root to the working directory
COPY src/ /src/
RUN ls -la /src/*

COPY src/data ./data
COPY src/intersavedmodel ./intersavedmodel
# COPY src/data/fouled_scaled ./fouled_scaled
# COPY src/data/data1.pickle ./data1.pickle

# Running Python Application
# CMD ["python3", "/src/main.py"]
# CMD ["python3", "/src/binaryClassifierSVM.py"]

# check_data_various_models.py
# CMD ["python3", "/src/check_data_various_models.py", "AlexNet", "data"]

# check_data_various_models_v3.py
# CMD ["python3", "/src/check_data_various_models_v3.py", "AlexNet", "data", "25","500"]
# Epoch, batch, k-fold crossvalidation
# CMD ["python3", "/src/check_data_various_models_v9.py", "AlexNet", "data", "5","500","5"]
# CMD ["python3", "/src/check_data_various_models_v7.py", "AlexNet", "data", "1","100","2"]
# Epoch, batch, total number of training files
# CMD ["python3", "/src/check_data_various_models_v11.py", "AlexNet", "data", "5","500","81"]
# CMD ["python3", "/src/check_data_various_models_v11.py", "AlexNet", "data", "10","500","81"]
# CMD ["python3", "/src/check_data_various_models_v11.py", "AlexNet", "data", "25","256","81"]
# CMD ["python3", "/src/check_data_various_models_v11.py", "AlexNet", "data", "20","32","81"]
# CMD ["python3", "/src/check_data_various_models_v11.py", "AlexNet", "data", "20","16","81"]
# CMD ["python3", "/src/check_data_various_models_v11.py", "AlexNet", "data", "200","16","81"]
# CMD ["python3", "/src/check_data_various_models_v11.py", "CNN", "data", "5","256","81"]


# python train_model.py -d <data dir> -n <num files of data> [-m] <model name> [-e] <num epochs> [-b] <batch size> [-lr] <learning_rate>
# CNN, AlexNet, AlexNetV2, or InceptionV3
CMD ["python3", "/src/train_model.py", "-d", "data", "-n","1","-m","InceptionV3","-e","3","-b","32","-lr","0.0001"]
# python train_model.py -d <data dir> -n <num files of data> [-m] <model name> [-e] <num epochs> [-b] <batch size> [-lr] <learning_rate>

# CMD ["python3", "/src/test.py", "data"]
