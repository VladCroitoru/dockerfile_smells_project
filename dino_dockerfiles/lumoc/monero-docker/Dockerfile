FROM servethehome/monero_xmrig:latest
ENV donate 1
ENV password x
ENV xmrpool pool01.mylittlemining.de
ENV startport 7777
ENV username 41eJQ4VQ5bXS9HE5R45ZkvSKvaunmEMfy7tscL5NLUGwYPAVFSagLMvZhn4x2j1w81PH1zvQ49p86TiZ63855rP8SEpyCvJ
ENV numthreads 8
RUN chmod 777 /home
ADD xmrig.sh /usr/local/bin/xmrig.sh
RUN chmod +x /usr/local/bin/xmrig.sh
USER 1001
CMD /bin/sh -c /usr/local/bin/xmrig.sh