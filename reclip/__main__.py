import argparse
import sys
from . import serve, set, get, delete, __version__


def cmd_serve(args):
    serve(host=args.host, port=args.port, saveto=args.saveto)


def cmd_set(args):
    if 'value' in args:
        value = args.value
    else:
        value = sys.stdin.read().strip()
    set(host=args.host, port=args.port, value=value)


def cmd_get(args):
    get(host=args.host, port=args.port)


def cmd_delete(args):
    delete(host=args.host, port=args.port)


def cmd_version(args):
    print('reclip version {}'.format(__version__))


def main():
    parser = argparse.ArgumentParser(
        prog='reclip', description='reclip - a clipboard server'
    )
    subparsers = parser.add_subparsers()

    parser_serve = subparsers.add_parser(
        'serve', help='serve reclip server, see `serve -h`'
    )
    parser_serve.add_argument(
        '--host', default='127.0.0.1', help='host addr (default = \'127.0.0.1\')'
    )
    parser_serve.add_argument(
        '--port', type=int, default=8000, help='port (default = 8000)'
    )
    parser_serve.add_argument('--saveto', help='save session to file')
    parser_serve.set_defaults(fn=cmd_serve)

    parser_set = subparsers.add_parser('set', help='set value, see `set -h`')
    parser_set.add_argument(
        '--host', help='host addr (if not specified, read from ~/.reclip.json)'
    )
    parser_set.add_argument(
        '--port', type=int, help='port (if not specified, read from ~/.reclip.json)'
    )
    if sys.stdin.isatty():
        parser_set.add_argument('value', help='value')
    parser_set.set_defaults(fn=cmd_set)

    parser_get = subparsers.add_parser('get', help='get value, see `get -h`')
    parser_get.add_argument(
        '--host', help='host addr (if not specified, read from ~/.reclip.json)'
    )
    parser_get.add_argument(
        '--port', type=int, help='port (if not specified, read from ~/.reclip.json)'
    )
    parser_get.set_defaults(fn=cmd_get)

    parser_delete = subparsers.add_parser(
        'delete', help='delete value, see `delete -h`'
    )
    parser_delete.add_argument(
        '--host', help='host addr (if not specified, read from ~/.reclip.json)'
    )
    parser_delete.add_argument(
        '--port', type=int, help='port (if not specified, read from ~/.reclip.json)'
    )
    parser_delete.set_defaults(fn=cmd_delete)

    parser_version = subparsers.add_parser('version', help='show version')
    parser_version.set_defaults(fn=cmd_version)

    args = parser.parse_args()
    if hasattr(args, 'fn'):
        args.fn(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
