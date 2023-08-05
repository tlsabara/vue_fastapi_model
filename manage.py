
import logging
import os
import argparse
import uvicorn

from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("runserver", help="inicia a aplicação", type=str)
    parser.add_argument("--port", help="porta de acesso", type=int, default=8000)

    args = parser.parse_args()

    if args.runserver == "runserver":
        logging.info(f'API on air! vs: {os.environ.get("API_VERSION")}')
        uvicorn.run(
            app="api.application:app",
            host="127.0.0.1",
            reload=True,
            port=args.port
        )

    print(args)
