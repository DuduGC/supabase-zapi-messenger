# Supabase Z-API Messenger

Projeto em Python que lê contatos do **Supabase** e envia mensagens personalizadas no **WhatsApp** usando a **Z-API**.

## Tecnologias

* Python
* Supabase
* Z-API
* Requests
* Python Dotenv

---

## Setup da tabela no Supabase

Crie uma tabela chamada:

```sql
Contatos
```

Com as colunas:

| Campo    | Tipo |
| -------- | ---- |
| id       | int8 |
| Nome     | text |
| Telefone | text |

Exemplo:

| id | Nome   | Telefone      |
| -- | ------ | ------------- |
| 1  | Rafael | 5511999999999 |

**Formato do telefone:**

```txt
5511999999999
```

Sem espaços, traços ou `+`.

---

## Variáveis de ambiente (.env)

Crie um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=sua_url
SUPABASE_KEY=sua_chave

ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
ZAPI_SECURITY_TOKEN=seu_security_token
```

---

## Instalação

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Como rodar

Execute o projeto:

```bash
python -m app.main
```

Saída esperada:

```txt
[SUCESSO] Mensagem enviada para Rafael
```
