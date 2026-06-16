# supabase-zapi-messenger

Serviço em Python que lê mensagens pendentes no Supabase e as envia via [Z-API](https://developer.z-api.io/) (WhatsApp).

## Estrutura

```
supabase-zapi-messenger/
├── app/
│   ├── main.py       # Loop principal de processamento
│   ├── database.py   # Cliente e queries Supabase
│   ├── sender.py     # Envio de mensagens via Z-API
│   └── config.py     # Variáveis de ambiente
├── .env
├── requirements.txt
└── venv/
```

## Pré-requisitos

- Python 3.11+
- Conta Supabase com tabela `messages`
- Instância Z-API configurada

### Tabela `messages` (exemplo)

```sql
create table messages (
  id uuid primary key default gen_random_uuid(),
  phone text not null,
  message text not null,
  status text not null default 'pending',
  error text,
  created_at timestamptz not null default now()
);
```

## Instalação

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt
```

Copie `.env` e preencha com suas credenciais.

## Execução

Na raiz do projeto:

```bash
python -m app.main
```

O serviço consulta mensagens com `status = 'pending'`, envia via Z-API e atualiza o status para `sent` ou `failed`.

## Variáveis de ambiente

| Variável | Descrição |
|----------|-----------|
| `SUPABASE_URL` | URL do projeto Supabase |
| `SUPABASE_KEY` | Chave de API (service role recomendada) |
| `ZAPI_INSTANCE_ID` | ID da instância Z-API |
| `ZAPI_TOKEN` | Token da instância |
| `ZAPI_CLIENT_TOKEN` | Client token (se exigido pela conta) |
| `POLL_INTERVAL_SECONDS` | Intervalo entre ciclos (padrão: 10) |
