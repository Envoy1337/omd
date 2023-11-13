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


if __name__ == '__main__':
    documents = ["""Crock Pot Pasta Never boil pasta again""",
                 """Pasta Pomodoro
                    Fresh ingredients Parmesan to taste"""]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(documents)
    print(count_matrix)
    print(vectorizer.get_feature_names())

