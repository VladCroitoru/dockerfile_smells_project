FROM planetcardano/cardano-base:1.2-3

WORKDIR /home/cardano/cardano-sl

RUN . /home/cardano/.nix-profile/etc/profile.d/nix.sh && nix-build -A connectScripts.mainnetWallet -o connect-to-mainnet
RUN sed -ur -i 's/--wallet-address 127.0.0.1/--wallet-address 0.0.0.0/' connect-to-mainnet

EXPOSE 8090

CMD ./connect-to-mainnet
