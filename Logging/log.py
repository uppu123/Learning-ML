import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers =[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger("Arithmetic App")


def add(a, b):
    logger.debug(f"Adding {a} and {b} = {a + b}")
    return a + b


def sub(a, b):
    logger.debug(f"Subtracting {a} and {b} = {a - b}")
    return a - b


def mult(a, b):
    logger.debug(f"Multiplying {a} and {b} = {a * b}")
    return a * b


def div(a, b):
    try:
        result = a / b
        logger.debug(f"Dividing {a} and {b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Error: Division by zero is not allowed.")
        raise


add(10,5)
sub(10,5)
mult(10,5)
div(10,5)