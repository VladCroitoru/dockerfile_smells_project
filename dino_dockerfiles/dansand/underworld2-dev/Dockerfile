FROM underworldcode/underworld2


# set working directory to /opt, and install underworld files there.
WORKDIR /opt

RUN pip install networkx
RUN pip install easydict
RUN pip install naturalsort
RUN pip install "networkx==1.11"
RUN pip install pint
RUN pip install pandas


USER root

RUN git clone https://github.com/dansand/UWsubduction.git

# change user and update pythonpath
ENV PYTHONPATH $PYTHONPATH:$UW2_DIR
#ENV PYTHONPATH /workspace/user_data/UWGeodynamics:$PYTHONPATH
ENV PYTHONPATH /opt/UWsubduction:$PYTHONPATH

# move back to workspace directory
WORKDIR /workspace


# CHANGE USER
USER $NB_USER
WORKDIR /workspace
