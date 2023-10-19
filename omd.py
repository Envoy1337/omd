class my_CountVectorizer:
    mp_words = []

    def my_fit_transform(self, text=None):
        res = []
        my_CountVectorizer.mp_words = []
        my_CountVectorizer.S = []
        for line in text:
            my_CountVectorizer.S.append(line)
            cur = line.lower()
            cur_s = cur.split()
            for i in range(len(cur_s)):
                if cur_s[i] not in my_CountVectorizer.mp_words:
                    my_CountVectorizer.mp_words.append(cur_s[i])
        for line in my_CountVectorizer.S:
            cur = line.lower()
            cur_s = cur.split()
            cur_res = [0] * len(my_CountVectorizer.mp_words)
            for j in range(len(my_CountVectorizer.mp_words)):
                cur_res[j] = cur_s.count(my_CountVectorizer.mp_words[j])
            res.append(cur_res)
        return res

    def my_get_feature_names(self):
        return my_CountVectorizer.mp_words
