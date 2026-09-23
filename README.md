# 🛒 Pedidos Messaging System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![RabbitMQ](https://img.shields.io/badge/RabbitMQ-3.x-orange.svg)](https://www.rabbitmq.com/)
[![Redis](https://img.shields.io/badge/Redis-7.x-red.svg)](https://redis.io/)

Sistema assíncrono de processamento de pedidos desenvolvido em **Python**, utilizando **RabbitMQ** como mensageria (broker) e **Redis** para gerenciamento de cache e estado rápido das transações.

---

## 📌 Sobre o Projeto

O projeto resolve o problema de processamento síncrono e gargalo na criação de pedidos em um e-commerce/plataforma de vendas. 

* **RabbitMQ:** Recebe a fila de novos pedidos, garantindo entrega confiável (*message broker*) e desacoplamento do backend.
* **Redis:** Armazena o pedido e faz cache de dados temporários para rápida leitura.
* **Python (Worker):** Consome e processa as filas de mensageria assincronamente.

---

## 🚀 Arquitetura do Fluxo

1. O cliente envia a requisição de **Criar Pedido**.
2. O evento do pedido é publicado na fila do **RabbitMQ**.
3. O **Worker Python** consome a mensagem da fila, executa a regra de negócio.
4. O pedido é atualizado no **Redis** ao final do processamento.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 
* **Broker / Filas:** RabbitMQ 
* **Cache / Estado:** Redis
* **Containerização:** Docker & Docker Compose

---

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
* [Git](https://git-scm.com)
* [Python 3.10+](https://www.python.org/)
* [Docker & Docker Compose](https://www.docker.com/)

---


```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
