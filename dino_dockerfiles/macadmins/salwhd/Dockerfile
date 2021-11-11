#Version: 0.0.2

FROM macadmins/sal

MAINTAINER Nick McSpadden "nmcspadden@gmail.com"

RUN git clone https://github.com/nmcspadden/Sal-WHDImport.git /home/docker/sal/whdimport
RUN git clone https://github.com/nmcspadden/MacModelShelf.git /home/docker/sal/macmodelshelf
RUN mv /home/docker/sal/macmodelshelf/macmodelshelf.py /home/docker/sal/
RUN mv /home/docker/sal/macmodelshelf/macmodelshelf.json /home/docker/sal/