FROM alpine AS grosse-montagne

COPY back /app
WORKDIR /app

# Installation des applications nécessaires
RUN apk add python3
RUN apk add py3-pip
RUN apk add nodejs
RUN apk add npm

# Installation des librairies
RUN pip install -r requirements.txt

WORKDIR /app/app-svelte
RUN npm i

# Execution du conteneur
WORKDIR /app
CMD [ "/bin/bash", "run.sh"]
