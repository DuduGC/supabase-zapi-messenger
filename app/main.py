from app.database import get_contacts
from app.sender import send_message


def main():

    contacts = get_contacts()

    if not contacts:
        print("Nenhum contato encontrado.")
        return

    for contact in contacts:

        nome = contact["nome"]
        telefone = contact["telefone"]

        status = send_message(
            telefone,
            nome
        )

        print(
            f"Mensagem enviada para "
            f"{nome}: {status}"
        )


if __name__ == "__main__":
    main()