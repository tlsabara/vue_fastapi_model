#!/usr/bin/python

import os
import argparse
import uvicorn

from api.application import __version__
from dotenv import load_dotenv

load_dotenv()

CLI_VERSION = __version__

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--runserver", help="inicia a aplicação", required=False, action="store_true")
    parser.add_argument("--port", help="porta de acesso", type=int, default=8000)
    parser.add_argument("--stage", help="stage de desenvolvimento", type=str, default="dev")
    parser.add_argument("--version", help="versão da aplicação", required=False, action="store_true")

    args = parser.parse_args()

    if args.version:
        print("API: ", CLI_VERSION)
        exit(0)

    if args.runserver and args.stage == "dev":
        print(f'API on air! vs: {os.environ.get("API_VERSION")}')
        uvicorn.run(
            app="api.application:app",
            host="127.0.0.1",
            reload=True,
            port=args.port
        )

    if args.runserver and args.stage == "prod":
        print(f'API on air! vs: {os.environ.get("API_VERSION")}')
        uvicorn.run(
            app="api.application:app",
            host="0.0.0.0",
            port=args.port
        )

    print(args)
