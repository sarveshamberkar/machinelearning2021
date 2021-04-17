import logging as lg
import employee

formatter = lg.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

stream_handler = lg.StreamHandler()
stream_handler.setFormatter(formatter)

logger = lg.getLogger(__name__)
logger.setLevel(lg.INFO)



file_handler = lg.FileHandler('logs/sample_log.log')
file_handler.setLevel(lg.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        print('zero division error')
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)

sub_result = subtract(num_1, num_2)


mul_result = multiply(num_1, num_2)


div_result = divide(num_1, num_2)
