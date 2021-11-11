FROM kunstmaan/explorer-multichain

ENV CHAINNAME        MainChain
ENV RPC_USER         multichainrpc
ENV RPC_PASSWORD     multichain123
ENV RUNTIME_PARAMS   -txindex -shrinkdebugfilesize

EXPOSE 8000
EXPOSE 9000
EXPOSE 7000

COPY runchain.sh /root/runchain.sh
CMD ["/bin/bash", "/root/runchain.sh"]
