#docker build -t shst .
#docker run -it --rm -v /local/path:/usr/node/ shst:latest /bin/bash
#docker run -it --rm -v /local/path:/usr/node/ shst:latest shst extract usr/node/boundary_ii.geojson --out=usr/node/ii.geojson --metadata --tile-hierarchy=8 --tiles
#docker run -it --rm -v /local/path:/usr/node/ shst:latest shst match /usr/node/point_1.in.geojson --out=/usr/node/out.geojson --tile-hierarchy=8

FROM node:10

ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin

USER node
RUN npm install -g sharedstreets@0.12.4
