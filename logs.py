import logging


class CustomFormatter(logging.Formatter):
    GREY = "\x1b[38;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"
    FORMAT = "%(asctime)s - %(name)s - # %(levelname)-8s - %(message)s | (%(filename)s:%(lineno)d)" # noqa

    FORMATS = {
        logging.DEBUG: GREY + FORMAT + RESET,
        logging.INFO: GREY + FORMAT + RESET,
        logging.WARNING: YELLOW + FORMAT + RESET,
        logging.ERROR: RED + FORMAT + RESET,
        logging.CRITICAL: BOLD_RED + FORMAT + RESET
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class LogConfig:
    """Класс конфигурации логирования
    setup_logging() - метод для настройки логирования
    """
    @staticmethod
    def setup_logging():
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setFormatter(CustomFormatter())
        root_logger.addHandler(ch)

        logging.getLogger('sqlalchemy.engine.Engine').disabled = True
        logging.getLogger('aiogram').setLevel(logging.WARNING)

        return logging.getLogger(__name__)
