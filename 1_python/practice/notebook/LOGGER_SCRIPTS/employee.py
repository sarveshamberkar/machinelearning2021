# import logging
import logging as lg


logger = lg.getLogger(__name__)
logger.setLevel(lg.INFO)

formatter = lg.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s') # file handler is used to format and not logger
file_handler = lg.FileHandler('logs/employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
#
# file_handler = logging.FileHandler('logs/employee.log')
# file_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')
