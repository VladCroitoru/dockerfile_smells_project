# docker build . -t wicebing/env-ehrs
# sudo docker run --gpus all -d -p 21111:22 -p 21112:8888 -v /home/bixa6000/ehrs:/root/data --name my_ehrs wicebing/env-ehrs:gpus
# sudo docker exec my_server cat /etc/hosts

# sudo rm -rf  /root/.ssh/known_hosts 
# ssh-keygen -f "/home/bixea6000/.ssh/known_hosts" -R "172.17.0.2"

# ssh root@172.17.0.2
# jupyter lab  --port=8888 --allow-root --ip=0.0.0.0

# remember to install the nvidia docker from the link [ref] 
# https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html

FROM nvidia/cuda:11.4.2-devel-ubuntu20.04
#FROM ubuntu:20.04
#FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-devel

#ENV DEBIAN_FRONTEND=noninteractive 
ARG DEBIAN_FRONTEND=noninteractive
  
RUN apt-get update \
    && apt-get install -y tzdata \ 
    && apt-get install -y openssh-server \
    && apt-get install -y wget \ 
    && apt-get install -y build-essential \
    && apt-get install -y screen \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /root/data

# -- install miniconda --
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-py39_4.10.3-Linux-x86_64.sh -b \
    && rm -f Miniconda3-py39_4.10.3-Linux-x86_64.sh \
    && echo ". /root/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "conda activate" >> ~/.bashrc
# -- install miniconda --


# -- install package --
RUN conda update --all -y \ 
    && python -m pip install --upgrade pip
RUN conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch -y
RUN python -m pip install transformers
RUN conda install -c conda-forge jupyterlab -y \
    && conda install -c conda-forge implicit -y \
    && conda install bottleneck -y \
    && conda install jupyter -y \
    && conda install matplotlib -y \ 
    && python -m pip install pandas requests tqdm seaborn tensorflow ipykernel keras lightgbm ipywidgets lxml numpy \
    && python -m pip install scikit-learn \
    && python -m pip install pyfolio xgboost
    
# -- install package --


# -- set ssh --
RUN mkdir /var/run/sshd \ 
    && echo 'root:bixe' | chpasswd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd \
    && echo "Port 22" >> /etc/ssh/sshd_config \
    && echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config \
    && echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

EXPOSE 22
# -- set ssh --

CMD ["/usr/sbin/sshd", "-D"]



    
    
    
    
    
    
    
    
    
    
# =====================
# RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
# ENV NOTVISIBLE "in users profile"
# RUN echo "export VISIBLE=now" >> /etc/profile
