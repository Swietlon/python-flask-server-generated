import connexion
import six

from swagger_server import util


def addition_get(x, y):  # noqa: E501
    """addition_get

    Returns sum of x and y # noqa: E501

    :param x: First element of sum
    :type x: float
    :param y: Second element of sum
    :type y: float

    :rtype: float
    """
    return str(x+y)


def division_get(x, y):  # noqa: E501
    """division_get

    Returns quotient of x and y # noqa: E501

    :param x: The dividend
    :type x: float
    :param y: The divider
    :type y: float

    :rtype: float
    """
    if y != 0:
        return str(x/y)
    return "wrong param"

def multiplication_get(x, y):  # noqa: E501
    """multiplication_get

    Returns product of x and y # noqa: E501

    :param x: First element of product
    :type x: float
    :param y: Second element of product
    :type y: float

    :rtype: float
    """
    return str(x*y)


def substraction_get(x, y):  # noqa: E501
    """substraction_get

    Returns the difference x and y # noqa: E501

    :param x: The minuend
    :type x: float
    :param y: The subtrahend
    :type y: float

    :rtype: float
    """
    return str(x-y)
