# Use uma imagem de python oficial como a base
FROM python:3.9

# Configurar a diretoria de trabalho
WORKDIR /app

# Copiar o arquivo .env para o contêiner
COPY ./backend/.env /app

# Copiar o código da aplicação para o contêiner
COPY ./backend/src /app

# Instalar as dependências
RUN pip install fastapi uvicorn[standard] python-jose[cryptography] passlib[bcrypt] swagger-ui-py && python -m pip install oracledb

# Definir variáveis de ambiente a partir do arquivo .env
ENV $(cat /app/.env | grep -v ^# | xargs)

# Comando para executar a aplicação
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
