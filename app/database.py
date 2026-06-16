from supabase import create_client
from app.config import (
    SUPABASE_URL,
    SUPABASE_KEY
)

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def get_contacts(limit=3):
    response = (
        supabase
        .table("Contatos")
        .select("*")
        .limit(limit)
        .execute()
    )

    return response.data