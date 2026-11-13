<div align="center">

# ⛵ EnjoyTagusOO

### Agendador de passeios de barco para a cooperativa *Tagus Sailing*

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Paradigma](https://img.shields.io/badge/Paradigma-Orientado%20a%20Objetos-8A2BE2)
![Cadeira](https://img.shields.io/badge/Cadeira-Programa%C3%A7%C3%A3o%202-orange)
![Ano](https://img.shields.io/badge/Ano%20letivo-2022%2F2023-blue)

</div>

---

## 📋 Informação do Projeto

| | |
|---|---|
| **Autores** | Pedro Rosa (60294) · Tomás Nogueira (60285) — Grupo 106 |
| **Data** | Ano letivo 2022/2023 (novembro de 2022) |
| **Cadeira** | Programação 2 — Programação Orientada a Objetos |
| **Instituição** | Faculdade de Ciências da Universidade de Lisboa (FCUL) |
| **Relatório** | [relGrupo106.pdf](relGrupo106.pdf) |

---

## 📖 Sobre

O **EnjoyTagusOO** gere o agendamento de passeios de barco no rio Tejo. A partir da lista atual de skippers, da agenda atual e de um conjunto de novos pedidos de clientes, atribui cada pedido ao skipper mais adequado e gera a **lista de skippers e a agenda atualizadas** para o período seguinte (30 minutos depois).

## ✨ Funcionalidades

- 🧱 **Design orientado a objetos** — classes Python seguindo *Design by Contract* (`Requires` / `Ensures`).
- 📅 **Gestão da agenda** — atualiza o calendário de passeios à medida que chegam pedidos e o tempo avança.
- 🧭 **Atribuição de skippers** — associa clientes a skippers por língua, categoria de licença e especialização.
- ⚖️ **Gestão de conflitos** — os passeios nunca se sobrepõem e os skippers nunca excedem as horas de trabalho.
- 🛡️ **Validação dos ficheiros** — verifica se o nome de cada ficheiro coincide com o cabeçalho (hora e âmbito).

## 🧠 Algoritmo de Atribuição

Cada pedido é atribuído a um skipper segundo estes critérios, por ordem:

1. **Capacidade** — fala a língua do cliente, tem a categoria de licença exigida e corresponde à especialização pedida (`speed`, `comfort` ou `price`).
2. **Disponibilidade** — o skipper que fica disponível mais cedo.
3. **Custo** — em caso de empate, o de menor preço por hora.
4. **Carga de trabalho** — em caso de empate, o que tem menos horas acumuladas.
5. **Nome** — desempate final por ordem alfabética.

Os pedidos que não podem ser atendidos aparecem na nova agenda como `not-assigned`.

---

## 🚀 Como Executar

### Requisitos

- **Python 3** (não são necessárias bibliotecas externas)

### 1. Clonar o repositório

```bash
git clone https://github.com/pedrorosa3/EnjoyTagusObjectOriented.git
cd EnjoyTagusObjectOriented
```

### 2. Executar o programa

```bash
python3 update.py <ficheiro_skippers> <ficheiro_agenda> <ficheiro_pedidos>
```

> No Windows, usa `python` ou `py` em vez de `python3`.

Os três ficheiros **têm de ser do mesmo período**, e a hora no nome de cada ficheiro tem de coincidir com a hora no seu cabeçalho (ex.: `skippers10h00.txt` → `Time: 10:00`).

### Exemplo

```bash
python3 update.py skippers10h00.txt schedule10h00.txt requests10h00.txt
```

Isto cria dois ficheiros novos para o período seguinte:

```
skippers10h30.txt
schedule10h30.txt
```

O repositório inclui outros exemplos de entrada: `10h00`, `13h00`, `17h00` e `18h00`.

---

## 📂 Formato dos Ficheiros de Entrada

Todos os ficheiros têm o mesmo cabeçalho:

```
Company:
Tagus Sailing
Day:
14:11:2022
Time:
10:00
<Secção>:
```

<details>
<summary><b>skippersHHhMM.txt</b></summary>

```
Skippers:
Carlota Castro, (english; portuguese), 2*, 50, price, 40, 20, (14:11:2022, 12:00)
```
Nome, línguas, categoria de licença, preço por hora, especialização, máx. de horas sem pausa, horas acumuladas, (disponível a partir de: data, hora)
</details>

<details>
<summary><b>scheduleHHhMM.txt</b></summary>

```
Schedule:
14:11:2022, 08:00, 4, Dinis Soares, 200, Franz Ferdinand
```
Data, hora de início, duração (horas), skipper, preço, cliente
</details>

<details>
<summary><b>requestsHHhMM.txt</b></summary>

```
Requests:
Dino Caprio, (english; italian), 2*, price, 4
```
Cliente, línguas, licença exigida, especialização, duração (horas)
</details>

---

## 🗂️ Estrutura do Projeto

```
EnjoyTagusObjectOriented/
├── update.py        # Ponto de entrada
├── Scheduling.py    # Algoritmo de atribuição (skippers ↔ pedidos)
├── Skipper.py       # Entidade skipper
├── Skippers.py      # Leitura/escrita do ficheiro de skippers
├── Request.py       # Entidade pedido
├── Requests.py      # Leitura do ficheiro de pedidos
├── Event.py         # Entidade passeio agendado
├── Schedule.py      # Leitura/escrita do ficheiro da agenda
├── NotAssigned.py   # Pedidos que não foi possível atribuir
├── DateTime.py      # Funções auxiliares de data/hora
├── Constants.py     # Constantes partilhadas
├── *.txt            # Ficheiros de exemplo (entrada/saída)
└── relGrupo106.pdf  # Relatório do projeto
```

---

<div align="center">

Feito por **Pedro Rosa** & **Tomás Nogueira** · FCUL · 2022/2023

</div>
