# Pull base pytorch image
FROM pytorch/pytorch:1.9.0-cuda10.2-cudnn7-devel

# Install repository specific dependencies
RUN pip install scipy
RUN pip install pandas
RUN pip install sklearn
RUN pip install matplotlib
RUN pip install kneed
RUN pip install scikit-image
RUN pip install tensorboard
RUN apt update && apt upgrade -y


# Define user to use (No root)
ARG HOST_USER_ID=37781
ARG HOST_USER_NAME=micheln
ARG HOST_GROUP_ID=513
ARG USER_DIR=/home/${HOST_USER_NAME}

RUN groupadd -g ${HOST_GROUP_ID} domain
RUN useradd -l -u ${HOST_USER_ID} -g domain ${HOST_USER_NAME}

#  Define working directory
WORKDIR ${USER_DIR}

# Fix permissions
RUN chown -R ${HOST_USER_NAME} ${USER_DIR}
RUN chgrp -R ${HOST_GROUP_ID} ${USER_DIR}

# Define mountable volumes
# Note VOLUME must
VOLUME ${USER_DIR}
