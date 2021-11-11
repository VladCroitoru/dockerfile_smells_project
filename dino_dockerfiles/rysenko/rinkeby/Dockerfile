FROM ethereum/client-go:stable
EXPOSE 8545
EXPOSE 30303
ENTRYPOINT ["geth", "--syncmode", "fast", "--rinkeby", "--cache", "2048", "--rpc",  "--rpcaddr", "0.0.0.0", "--rpccorsdomain" , "*", "--rpcvhosts", "*",  "--rpcapi", "eth,net,web3,personal,debug"]
