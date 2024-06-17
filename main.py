import argparse
import dotenv

import os

from services.lyrics_service import get_lyrics
from services.openai_service import explain_music_by_ai



if __name__ == "__main__":
    dotenv.load_dotenv()

    aiml_api_key = os.getenv("AI_ML_API_KEY")

    print("Resumo de Letras de Música")

    argparser = argparse.ArgumentParser(
        prog="explain-music",
        description="Aplicação que resume e explica letras de músicas",
        epilog="Ajuda"
    )

    argparser.add_argument("--artista", required=True, type=str)
    argparser.add_argument("--musica", required=True, type=str)

    args = argparser.parse_args()

    artista = args.artista
    musica =  args.musica

    print(f"Artista: {artista}, Música: {musica}")

    lyrics = get_lyrics(artista, musica)

    explain_music_by_ai(aiml_api_key, lyrics)

 





