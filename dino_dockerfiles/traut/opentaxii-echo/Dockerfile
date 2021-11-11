FROM intelworks/opentaxii

# Install Requirements
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && rm -f requirements.txt \
    && mkdir /install_dir 

# Setup Echo Persistence API
COPY ./ /install_dir
RUN cd /install_dir \
    && python setup.py install \
    && cd / \
    && rm -rf /install_dir

# Set Default Configuration
COPY ./opentaxii-config.yml /input/opentaxii.yml
