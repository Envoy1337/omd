from math import log


class CountVectorizer:
    def __init__(self):
        self.voc = {}
        self.mp_words  = []

    def fit_transform(self, corpus):
        """Подсчет частоты каждого слова в документах"""
        for corp in corpus:
            words = corp.split()
            for cur in words:
                if cur not in self.voc:
                    self.voc[cur] = len(self.voc)
        count_matrix = []
        for corp in corpus:
            count = [0] * len(self.voc)
            words = corp.split()
            for word in words:
                count[self.voc[word]] += 1
            count_matrix.append(count)

        return count_matrix

    def get_feature_names(self):
        """Получаем слова в порядке их появления в словаре"""
        self.mp_words = [word for word, _ in self.voc.items()]
        return self.mp_words


# number 2
def tf_transform(count_matrix:list[list[int]])->list[list[float]]:
    return [[el/sum(line) for el in line] for line in count_matrix]


# number 3
def idf_transform(count_matrix:list[list[int]]):
    num_uniq = len(count_matrix)
    n = len(count_matrix[0])
    idf = [sum([1 if row[i] else 0 for row in count_matrix]) for i in range(n)]
    idf = [log((num_uniq+1)/(el+1))+1 for el in idf]
    return idf


# number 4
class TfIdfTransformer:
    def init(self):
        pass

    def fit_transform(self, count_matrix: list[list[int]]) -> list[list[float]]:
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        res = []
        for row in tf:
            res.append([round(a * b, 3) for a, b in zip(row, idf)])
        return res

    @staticmethod
    def tf_transform(matrix: list[list[int]]) -> list[list[float]]:
        return [[round(x / sum(row), 3) for x in row] for row in matrix]

    @staticmethod
    def idf_transform(matrix: list[list[int]]) -> list[float]:
        new_matrix = [0] * len(matrix[0])
        for row in matrix:
            for idx, el in enumerate(row):
                if el > 0:
                    new_matrix[idx] += 1
        text_count = len(matrix)
        return [round(log((text_count + 1) / (x + 1)), 3) + 1 for x in new_matrix]


# number 5
class Tfidfvectorizer(CountVectorizer):
    def __init__(self, tf_class=TfIdfTransformer):
        super().__init__()
        self.tf_idf_transformer = TfIdfTransformer()

    def fit_transformm(self, corpus: list[str]):
        count_matrix_numbers = super().fit_transform(corpus)
        return self.tf_idf_transformer.fit_transform(count_matrix_numbers)


if  __name__ == '__main__':
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    print(tf_transform(count_matrix))
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    print(idf_transform(count_matrix))
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    tfidf = TfIdfTransformer()
    print(tfidf.fit_transform(count_matrix))
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = Tfidfvectorizer()
    tfidf_matrix = vectorizer.fit_transformm(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)


