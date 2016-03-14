import argparse
import json
import logging
import os

from blog_aggregator import BlogAggregator

logger = logging.getLogger()


def get_arguments():
    """Get user input as command line arguments"""
    parser = argparse.ArgumentParser(description='Blog aggregator')
    parser.add_argument(
        '-i',
        '--input',
        action='store',
        default='input.html',
        dest='input_file',
        help="input file"
    )
    parser.add_argument(
        '-o',
        '--output',
        action='store',
        default='output.json',
        dest='output_file',
        help="output file"
    )
    parser.add_argument(
        '-log',
        '--log-level',
        action='store',
        default='INFO',
        dest='log_level',
        help="console log level: DEBUG | INFO | WARNING | ERROR | CRITICAL | NOTSET (default: INFO)"
    )
    return parser.parse_args()


def configure_logging(log_level="INFO"):
    """Configure logging handler to standard error"""
    numeric_log_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_log_level, int):
        raise ValueError('Invalid log level: %s' % log_level)

    logger.setLevel(numeric_log_level)
    ch = logging.StreamHandler()
    ch.setLevel(numeric_log_level)
    formatter = logging.Formatter(
        fmt='[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        datefmt='%y%m%d %H:%M:%S'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def check_user_input(input_file, output_file):
    """Check user input"""
    if os.path.exists(input_file) is False:
        raise ValueError("Input file '%s' does not exists!" % input_file)

    if os.path.exists(os.path.dirname(output_file)) is False:
        logger.info("Output directory '%s' does not exists, creating folder structure!" %
                       os.path.dirname(output_file))
        os.makedirs(os.path.dirname(output_file))


def main():
    args = get_arguments()
    configure_logging(args.log_level)

    input_file = os.path.abspath(args.input_file)
    output_file = os.path.abspath(args.output_file)
    check_user_input(input_file, output_file)

    logger.info("Process started with input file '%s'" % input_file)

    blog_aggregator = BlogAggregator(input_file)
    feeds = blog_aggregator.aggregate()
    with open(output_file, 'w') as fp:
        json.dump(feeds, fp, indent=4, sort_keys=True, encoding='utf-8')

    logger.info("Process finished, the results are in output file '%s'" % output_file)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(e)
