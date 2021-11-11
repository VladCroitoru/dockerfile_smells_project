FROM kriansa/insurgency-server:2018-12-24
LABEL maintainer="Daniel Pereira <daniel@garajau.com.br>"

# Runtime settings
ENV RCON_PASSWORD=""
ENV SV_PASSWORD=""
ENV MAPNAME="market_coop checkpoint"
ENV MAPCYCLEFILE="mapcycle_checkpoint.txt"

# Force installation of workshop content
# sv_pure has to come first otherwise it will fail to download workshop files
# and the client will see "success failure" glowing sprites
ADD --chown=steam:steam game/subscribed_file_ids.txt insurgency/
RUN ./srcds_linux +sv_pure 0 -workshop +quit || true

# Send our custom files to the server
ADD --chown=steam:steam game/cfg/* insurgency/cfg/
ADD --chown=steam:steam game/addons insurgency/addons

# Run command with workshop support and tweaking it to Checkpoint Fun mode
# sv_pure and mapcyclefile have to be set on CLI
CMD ./srcds_linux -port 27015 -ip 0.0.0.0 -workshop \
   +rcon_password "$RCON_PASSWORD" +sv_password "$SV_PASSWORD" \
   +maxplayers $MAXPLAYERS +map $MAPNAME \
   +mapcyclefile "$MAPCYCLEFILE" +sv_pure 0
