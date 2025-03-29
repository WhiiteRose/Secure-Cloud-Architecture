FROM alpine AS grosse-montagne

COPY . /app
WORKDIR /app

# Installation des applications nécessaires
RUN apk add python3
RUN apk add py3-pip
RUN apk add nodejs
RUN apk add npm

# Installation des librairies
WORKDIR /app/back
RUN pip install -r requirements.txt

WORKDIR /app/back/app-svelte
RUN npm i
