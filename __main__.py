import argparse
import logging

from blog_aggregator import BlogAggregator


logger = logging.getLogger()


def get_arguments():
    parser = argparse.ArgumentParser(description='Blog aggregator')
    parser.add_argument(
        '-i',
        '--input',
        action='store',
        default='/data/input',
        dest='input',
        help="input file or directory"
    )
    parser.add_argument(
        '-o',
        '--output',
        action='store',
        default='/data/output',
        dest='output',
        help="output file or directory"
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
    numeric_log_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_log_level, int):
        raise ValueError('Invalid log level: %s' % log_level)

    logger.setLevel(numeric_log_level)
    ch = logging.StreamHandler()
    ch.setLevel(numeric_log_level)
    formatter= logging.Formatter(
        fmt='[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        datefmt='%y%m%d %H:%M:%S'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def main():
    args = get_arguments()
    configure_logging(args.log_level)
    logger.info('info')

    blog_aggregator = BlogAggregator('index.html')
    print blog_aggregator.get_links()

if __name__ == '__main__':
    main()