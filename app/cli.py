import argparse
import json

from app.service import VisionService

parser = argparse.ArgumentParser()

parser.add_argument(
    "--image",
    help="Image path"
)

parser.add_argument(
    "--question",
    help="Question"
)

args = parser.parse_args()


def pretty(result):

    print(
        json.dumps(result, indent=2)
    )


if args.image and args.question:

    result = VisionService.process(
        args.image,
        args.question
    )

    pretty(result)

else:

    parser.print_help()
