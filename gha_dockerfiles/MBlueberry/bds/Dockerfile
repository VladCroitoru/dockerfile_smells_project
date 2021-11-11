FROM shrbox/winehq:main

VOLUME [ "/home/container" ]
ENV BDSDIR /home/container/bds/
ENV BDSVER 1.17.11.01
ENV LLVER 1.1.2.1
RUN useradd -m bds -d /home/container -s /bin/bash && apt install wget unzip -y
USER container
WORKDIR /home/container/
RUN wget https://minecraft.azureedge.net/bin-win/bedrock-server-${BDSVER}.zip && \
wget https://github.com/LiteLDev/LiteLoaderBDS/releases/download/${LLVER}/LiteLoader.zip && \
unzip bedrock-server-${BDSVER}.zip -d ${BDSDIR} && \
unzip LiteLoader.zip -d ${BDSDIR} && \
rm /home/container/bedrock-server-${BDSVER}.zip && \
rm /home/container/LiteLoader.zip
WORKDIR ${BDSDIR}
COPY vcruntime140_1.zip ${BDSDIR}
COPY SymDB2_Old.exe ${BDSDIR}
RUN unzip vcruntime140_1.zip "vcruntime140_1.dll" && \
rm vcruntime140_1.zip && \
wine SymDB2_Old.exe && \
rm PDB_Symdef.txt && \
rm /home/container/.wine -r

ENV WINEDEBUG -all
CMD [ "wine", "/container/bedrock_server.exe" ]
