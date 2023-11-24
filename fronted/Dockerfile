FROM ubuntu
FROM node

COPY . /fronted

WORKDIR /fronted

RUN npm install
CMD ["npm", "run", "dev"]