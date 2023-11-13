import unittest


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


class TestFitTransform(unittest.TestCase):

    def test_fit_transform_single_arg(self):
        result = fit_transform('a', 'b', 'a', 'c')
        expected = [('a', [0, 0, 1]), ('b', [0, 1, 0]), ('a', [0, 0, 1]), ('c', [1, 0, 0])]
        self.assertEqual(result, expected)

    def test_fit_transform_iterable_arg(self):
        result = fit_transform(['a', 'b', 'c', 'a'])
        expected = [('a', [0, 0, 1]), ('b', [0, 1, 0]), ('c', [1, 0, 0]), ('a', [0, 0, 1])]
        self.assertEqual(result, expected)

    def test_fit_transform_assertNotIn(self):
        result = fit_transform('a', 'b', 'a', 'c')
        for item in result:
            self.assertNotIn('d', item[0])

    def test_fit_transform_invalid_input(self):
        with self.assertRaises(TypeError):
            fit_transform(123)


if __name__ == '__main__':
    unittest.main()
