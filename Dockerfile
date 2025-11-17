FROM python:3.11-slim

WORKDIR /app

# instalar dependências de build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copiar requirements
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# copiar o restante da aplicação
COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
