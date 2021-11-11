FROM python:3.6

VOLUME /logs

ENV WORKSPACE=/opt/VFB

ENV VFB_OWL_VERSION=Current

ENV CHUNK_SIZE=1000

ENV PING_SLEEP=120s

ENV BUILD_OUTPUT=${WORKSPACE}/build.out

ENV RUN_add_refs_for_anat=true
ENV RUN_import_pub_data=true
ENV RUN_make_named_edges=true
ENV RUN_KB2Prod=true
ENV RUN_add_constraints_and_redundant_labels=true
ENV RUN_Owl2neolabels=true

RUN pip3 install wheel
RUN pip3 install requests
RUN pip3 install psycopg2
RUN pip3 install pandas

RUN apt-get -qq update || apt-get -qq update && \ 
apt-get -qq -y install git curl wget default-jdk pigz maven libpq-dev python-dev tree gawk

ENV KBSERVER=http://kb.virtualflybrain.org

ENV PDBSERVER=http://pdb.virtualflybrain.org

ENV OWLSERVER=http://owl.virtualflybrain.org

ENV PDBuser=neo4j

ENV PDBpassword=password

ENV KBuser=neo4j

ENV KBpassword=password

COPY process.sh /opt/VFB/process.sh

COPY runsilent.sh /opt/VFB/runsilent.sh

RUN chmod +x /opt/VFB/*.sh

RUN echo -e "travis_fold:start:processLoad" && \
cd "${WORKSPACE}" && \
echo '** Git checkout VFB_neo4j **' && \
git clone --quiet https://github.com/VirtualFlyBrain/VFB_neo4j.git 

RUN pip3 install -r ${WORKSPACE}/VFB_neo4j/requirements.txt

RUN cd "${WORKSPACE}" && \
echo '** Git checkout VFB_connect **' && \
git clone --quiet https://github.com/VirtualFlyBrain/VFB_connect.git

RUN pip3 install -r ${WORKSPACE}/VFB_connect/requirements.txt

RUN cd ${WORKSPACE} && \
echo -e "travis_fold:end:processLoad"

RUN echo -e "travis_fold:start:sourcetree" && tree ${WORKSPACE} && echo -e "travis_fold:end:sourcetree"

ENV PYTHONPATH=${WORKSPACE}/VFB_neo4j/src/:${WORKSPACE}/VFB_connect/src/

CMD ["/opt/VFB/process.sh"]
