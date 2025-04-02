FROM alpine AS grosse-montagne

EXPOSE 80

COPY . /app
WORKDIR /app

# Installation des applications nécessaires
RUN apk add python3
RUN apk add py3-pip
RUN apk add nodejs
RUN apk add npm

# Installation des librairies
RUN pip install --break-system-packages -r requirements.txt

WORKDIR /app/app-svelte
RUN npm i
RUN npm run build

# Execution du conteneur
WORKDIR /app
CMD ["/usr/bin/env", "python3", "app.py"]
