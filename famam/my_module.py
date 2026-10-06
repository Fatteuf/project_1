"""This module shows you how you can construct a nice documentation with
sphinx and the right syntaxe for docstrings.
"""

import numpy as np


def typed_function(a: np.ndarray, b: str = "") -> bool:
    r"""This is a typed function.
    This docstring is made so that it renders nicely on sphinx. It features notes,
    arguments, cross references (here, to numpy documentation), maths and examples.

    Notes:
        - This is a section with multiple notes
        - This second note has maths! :math:`p \in \mathbb{N}`

    .. math::
        :label: equation1

        D = \sum_{0 \le i < p} \alpha_i

    Args:
        a: first parameter, its description is really, and fits in
            two lines (note the indentation). The object must be a :obj:`np.ndarray`
        b: second parameter. Defaults to empty string.

    Examples
        >>> typed_function(np.zeros(10))
        False

        >>> typed_function(
        ...     np.zeros(10),
        ...     "hello"
        ... )
        False

    Returns:
        Always return False, it's not a very interesting function. See :eq:`equation1`
        for some more maths.
    """
    return False


def add_numbers(a: float, b: float) -> float:
    """Add two numbers.

    This function is a simple example, added to practice opening a pull request.

    Args:
        a: first number.
        b: second number.

    Examples
        >>> add_numbers(2, 3)
        5

        >>> add_numbers(-1.5, 1.5)
        0.0

    Returns:
        The sum of ``a`` and ``b``.
    """
    return a + b


def other_function() -> None:
    """This is another function

    This function is here to show you how sphinx displays functions of a same module
    in a webpage.
    """
