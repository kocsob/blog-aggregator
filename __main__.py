import logging


logger = logging.getLogger()


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
    configure_logging()
    logger.info('info')

if __name__ == '__main__':
    main()