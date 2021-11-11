#######################
# Base settings
#######################

# set base image (host OS)
FROM python:3.8
# FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

#######################
# Install dependencies
#######################

# set the working directory in the container
WORKDIR /imotion

# get model from online gdrive folder
# note: if the file disappears from gdrive...
# - uncomment this line
# - train an artemis model yourself
# - and put it in the folder: ./server/checkpoints/best_model.pt
RUN pip install gdown
RUN gdown https://drive.google.com/uc?id=1MvEBUqFCDflL-Y8TllzYUe_-rivb8bmF \
    && mkdir -p ./server/checkpoints/ \
    && mv best_model.pt ./server/checkpoints/best_model.pt

# install artemis dependencies first
COPY artemis/ ./artemis/
RUN pip install -e ./artemis/

# install imotion dependencies
COPY setup.py ./
RUN pip install -e .

# install corpora
RUN python -m textblob.download_corpora

# cold run image captioning, because it will download additional vocabulary files
COPY server/ ./server/
RUN python -m server.image_captioning

# copy all other files over
COPY . .

#######################
# Expose program
#######################

# command to run on container start
CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0"]
