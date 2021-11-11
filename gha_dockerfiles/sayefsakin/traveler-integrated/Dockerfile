FROM stevenrbrandt/phylanx.test:working

USER root
RUN echo jovyan:fishfood77 | chpasswd

# Fix otf2 path
ENV PATH="/usr/local/otf2/bin:${PATH}"

# Set up traveler-integrated
WORKDIR /
COPY . /traveler-integrated
WORKDIR /traveler-integrated
RUN find . | xargs chown jovyan
RUN pip3 install -r requirements.txt
EXPOSE 8000

# Set up jupyter
RUN pip3 install jupyter requests
EXPOSE 8789

WORKDIR /files
# COPY sweetnsassy.py ./
# COPY config.py ./
WORKDIR /traveler-integrated

RUN chown jovyan ~jovyan/.bashrc
RUN dnf install -y jq
WORKDIR /
RUN git clone https://github.com/TACC-Cloud/tapis-cli-ng
WORKDIR /tapis-cli-ng
RUN pip3 install --upgrade .
RUN ln -s /tapis-cli-ng /usr/local/cli
RUN dnf install -y glibc-langpack-en
ENV LC_ALL en_US.utf8

USER jovyan
WORKDIR /home/jovyan
RUN git clone https://github.com/stevenrbrandt/workenv.git
WORKDIR /home/jovyan/workenv
RUN python3 install.py
WORKDIR /traveler-integrated/notebook
ENV PATH /usr/local/cli/bin:/traveler-integrated/notebook/agave-cli/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# Default container command is to launch jupyter
CMD ["bash", "/traveler-integrated/jupyter.sh"]
