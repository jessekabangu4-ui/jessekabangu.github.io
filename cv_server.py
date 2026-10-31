from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser(description="Serveur HTTP pour le portfolio et le CV.")
    parser.add_argument("--host", default="0.0.0.0", help="Adresse IP d'écoute. Par défaut: 0.0.0.0")
    parser.add_argument("--port", type=int, default=8000, help="Port TCP. Par défaut: 8000")
    parser.add_argument("--directory", default=str(Path(__file__).resolve().parent), help="Répertoire à servir")
    args = parser.parse_args()

    directory = Path(args.directory).resolve()
    if not directory.exists():
        raise FileNotFoundError(f"Le dossier n'existe pas : {directory}")

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(directory), **kwargs)

    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Serveur lancé sur http://{args.host}:{args.port}")
    print(f"Dossier servi : {directory}")
    print(f"CV accessible : http://localhost:{args.port}/Jesse_up_cv.pdf")
    print("Appuyez sur Ctrl+C pour arrêter le serveur.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
