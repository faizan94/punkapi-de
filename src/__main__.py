"""
Main
----
"""
import json
import argparse
from src import __version__
from src import punk_requests


def parse_arguments():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('src')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('--file', '-f', help='Write output to file (file name)',
                        type=str, default='', required=False)

    sub_parser = parser.add_subparsers(dest='sub', required=True)

    by_name = sub_parser.add_parser('byname',
                                    help='String beer name information as partial or full match')
    by_name.add_argument('--name', '-n', type=str, help='Name as string', required=True)

    by_id = sub_parser.add_parser('byid', help='Str exact id or ids in (id|id|...) format')
    by_id.add_argument('--id', '-i', type=str, help='id as string', required=True)

    by_food = sub_parser.add_parser('byfood',
                                    help='String beer search by food pairs information as '
                                         'partial or full match')
    by_food.add_argument('--food-pairs', '-f', type=str, help='Food as string', required=True)

    by_id = sub_parser.add_parser('byinterval', help='Get beer brewed in interval')
    by_id.add_argument('--from-date', '-fd', type=str, help='date i.e. 10-11', required=True)
    by_id.add_argument('--until-date', '-ud', type=str, help='date i.e. 10-11', required=True)

    return parser.parse_args()


def request_result(output: json, file_path: str):
    """
    Show result in file on on terminal
    """
    if file_path == '':
        print(json.dumps(output, indent=4))
    else:
        with open(file_path, "w") as file:
            file.write(json.dumps(output, indent=4))


def main():
    """
    Main entry point for your project.
    """
    args = parse_arguments()
    if args.sub == 'byname':
        request_result(punk_requests.get_beer_by_name(args.name), args.file)
    elif args.sub == 'byid':
        request_result(punk_requests.get_beer_by_id(args.id), args.file)
    elif args.sub == 'byinterval':
        request_result(punk_requests.get_beer_brewed_in(args.from_date, args.until_date), args.file)
    elif args.sub == 'byfood':
        request_result(punk_requests.get_beer_by_food(args.food_pairs), args.file)


if __name__ == '__main__':
    main()
