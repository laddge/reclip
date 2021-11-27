import argparse
from . import serve, set, get, delete


def cmd_serve(args):
    serve(host=args.host, port=args.port)


def cmd_set(args):
    set(host=args.host, port=args.port)


def cmd_get(args):
    get(host=args.host, port=args.port)


def cmd_delete(args):
    delete(host=args.host, port=args.port)


def main():
    parser = argparse.ArgumentParser(prog='reclip', description='reclip - a clipboard server')
    subparsers = parser.add_subparsers()

    parser_serve = subparsers.add_parser('serve', help='see `serve -h`')
    parser_serve.add_argument('--host', default='127.0.0.1', help='host addr (default = \'127.0.0.1\')')
    parser_serve.add_argument('--port', default=8000, help='port (default = 8000)')
    parser_serve.set_defaults(fn=cmd_serve)

    parser_set = subparsers.add_parser('set', help='see `set -h`')
    parser_set.add_argument('--host', default='127.0.0.1', help='host addr (default = \'127.0.0.1\')')
    parser_set.add_argument('--port', default=8000, help='port (default = 8000)')
    parser_set.add_argument('content', help='content')
    parser_set.set_defaults(fn=cmd_set)

    parser_get = subparsers.add_parser('get', help='see `get -h`')
    parser_get.add_argument('--host', default='127.0.0.1', help='host addr (default = \'127.0.0.1\')')
    parser_get.add_argument('--port', default=8000, help='port (default = 8000)')
    parser_get.set_defaults(fn=cmd_get)

    parser_delete = subparsers.add_parser('delete', help='see `delete -h`')
    parser_delete.add_argument('--host', default='127.0.0.1', help='host addr (default = \'127.0.0.1\')')
    parser_delete.add_argument('--port', default=8000, help='port (default = 8000)')
    parser_delete.set_defaults(fn=cmd_delete)

    args = parser.parse_args()
    if hasattr(args, 'fn'):
        args.fn(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
