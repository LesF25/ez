FROM node:18-alpine

WORKDIR /app

RUN npm install -g @quasar/cli

COPY package*.json ./

RUN npm install

COPY . .

CMD ["quasar", "dev", "-m", "spa"]
