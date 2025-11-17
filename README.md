# Desafio-final-devops
# 🚀 Desafio Final – Pipeline DevOps (Build, Test e Deploy)

Este repositório contém o projeto final da disciplina de **DevOps**, cujo objetivo foi construir uma **pipeline completa de CI/CD** utilizando **GitHub Actions**, integrando processos de Build, Teste e Deploy de uma API Python Flask hospedada na plataforma **Render**.

---

## 📝 Objetivo do Desafio

Implementar uma pipeline DevOps contemplando:

1. **Build**  
   Preparação do ambiente, instalação de dependências e validação da aplicação.

2. **Testes Unitários**  
   Implementação de **3 testes unitários** para validar funcionalidades essenciais da API.

3. **Deploy Automatizado**  
   Publicação da aplicação na nuvem utilizando a plataforma **Render**.

---

## 📌 Tecnologias Utilizadas

- **Python 3.9**
- **Flask**
- **Unittest (testes unitários)**
- **Dockerfile / Docker Compose**
- **GitHub Actions** (CI/CD)
- **Render** (nuvem escolhida para o deploy)
- **YAML** (workflows)

---

## 🗂 Estrutura do Projeto

/
├── app.py # API Flask
├── requirements.txt # Dependências Python
├── test_app.py # Testes unitários
├── docker-compose.yml
├── Dockerfile
├── static/ # Arquivos estáticos (se usados)
├── .github/
│ └── workflows/
│ ├── deploy.yml # Pipeline principal CI/CD
│ └── test-trigger.yml # Workflow de teste


---

## ▶️ Como rodar o projeto localmente

### 1️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Executar a aplicação
python app.py

🧪 Como executar os testes

Foram desenvolvidos 3 testes unitários, localizados no arquivo test_app.py.

Rodar os testes:

python -m unittest discover


ou

python test_app.py


Se todos os testes passarem, a pipeline segue para o deploy.

🔄 Pipeline CI/CD – GitHub Actions

A pipeline está localizada em:

.github/workflows/deploy.yml


O workflow segue 3 etapas principais:

✔ 1. Build

Configura o Python

Instala dependências

Verifica estrutura do código

✔ 2. Test

Executa os 3 testes unitários

Se qualquer teste falhar → o deploy é bloqueado

✔ 3. Deploy

Se os testes passarem, o GitHub Actions dispara automaticamente um deploy hook para a plataforma Render.