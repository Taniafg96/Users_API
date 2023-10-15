import logging.config

class Logger:
    def __init__(self, name):
        self.logger_info = logging.getLogger('loggerInfo')
        self.logger_debug = logging.getLogger('loggerDebug')
        self.logger_warning = logging.getLogger('loggerWarning')
        self.logger_error = logging.getLogger('loggerError')
        self.logger_critical = logging.getLogger('loggerCritical')

        self.logger_info.name = name
        self.logger_debug.name = name
        self.logger_warning.name = name
        self.logger_error.name = name
        self.logger_critical.name = name

        logging.config.fileConfig('config/logging.conf', disable_existing_loggers=False)

    def debug(self, message):
        self.logger_debug.debug(message)
        
    def info(self, message):
        self.logger_info.info(message)
        
    def warning(self, message):
        self.logger_warning.warning(message)
        
    def error(self, message):
        self.logger_error.error(message)
        
    def critical(self, message):
        self.logger_critical.critical(message)