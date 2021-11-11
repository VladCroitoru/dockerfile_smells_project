FROM ubuntu

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y libpython-dev python-numpy python-leveldb python-pip git
RUN pip2 install m3-cdecimal

ENV code_dir /opt/augur_src
RUN mkdir $code_dir
WORKDIR $code_dir

# get all python installations done before importing code
ADD requirements.txt $code_dir/requirements.txt
RUN pip install -r requirements.txt

# Add code from current repo
ADD augur_ctl $code_dir/augur_ctl
ADD augur $code_dir/augur

# Allow access to external clients, required for host machine access
RUN sed -i "s/host='127\.0\.0\.1'/host='0.0.0.0'/" augur/augur.py

# trigger install, so changes get saved in image
RUN python -c "from augur import augur"

EXPOSE 9000
CMD ["./augur_ctl", "start"]
