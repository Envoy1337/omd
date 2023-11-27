def fit_transform(*args: str):
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


import pytest


def test_one_argument_string():
    result = fit_transform('a', 'b', 'c')
    assert result == [('a', [0, 0, 1]), ('b', [0, 1, 0]), ('c', [1, 0, 0])]


def test_one_argument_list():
    result = fit_transform(['x', 'y', 'z'])
    assert result == [('x', [0, 0, 1]), ('y', [0, 1, 0]), ('z', [1, 0, 0])]


def test_empty_input():
    with pytest.raises(TypeError):
        fit_transform()


def test_invalid_input_type():
    with pytest.raises(TypeError):
        fit_transform(123, 456)
