def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    :param obj: The object to be checked.
    :param a_class: The specified class to check against.
    :return: True if the object is an instance of a subclass of the specified class, otherwise False.
    """
    return issubclass(type(obj), a_class)
