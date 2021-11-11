FROM ubuntu:14.04
RUN apt update; apt install -y wget flex bison build-essential python-numpy cmake python-dev sqlite3 libsqlite3-dev libboost-dev libboost-system-dev libboost-thread-dev libboost-serialization-dev libboost-python-dev libboost-regex-dev
RUN cd; wget https://github.com/rdkit/rdkit/archive/Release_2015_09_2.tar.gz; tar xf Release_2015_09_2.tar.gz; cd rdkit-Release_2015_09_2; mkdir build; cd build; cmake ..
RUN cd ~/rdkit-Release_2015_09_2/build; make
#RUN make install

# matplotlib and jupyter
#RUN apt-get install -y libfreetype6-dev libpng-dev pkg-config pandoc libjpeg-dev zlib1g-dev
#RUN wget https://bootstrap.pypa.io/get-pip.py; python get-pip.py; pip install matplotlib jupyter Pillow

#EXPOSE 8888
#CMD PYTHONPATH=~/rdkit-Release_2015_09_2/ LD_LIBRARY_PATH=~/rdkit-Release_2015_09_2/lib jupyter-notebook --notebook-dir='/root' --no-browser --ip='*' --port 8888
