from palindrome.linkedstack import LinkedStack


class PalindromADT:
    def __init__(self):
        self.words = []
        self.palindroms = []

    def read(self, path, clear_row=lambda line: line.strip()):
        with open(path) as f:
            words = map(clear_row, f.readlines())
            self.words.append(words)

    @staticmethod
    def _is_palindrom(word):
        ls = LinkedStack()
        for i in range(len(word) // 2):
            ls.add(word[i])
        md = len(word) // 2 if len(word) % 2 == 0 else len(word) // 2 + 1
        for i in range(md, len(word)):
            if ls.pop() != word[i]:
                return False
        return True

    def process(self):
        self.palindroms = []
        for word in self.words:
            if PalindromADT._is_palindrom(word):
                self.palindroms.append(word)

    def write(self, path):
        data = list(map(lambda word: f"{word}\n", self.palindroms))
        with open(path, "w") as f:
            f.writelines(data)


if __name__ == "__main__":
    pl = PalindromADT()
    pl.read("data/in/words.txt")
    pl.process()
    pl.write("data/out/new_words.txt")
    pl.read("data/in/base.lst", lambda x: x.strip().split(" ")[0])
    pl.process()
    pl.write("data/out/new_base.txt")
    # ls = LinkedStack()
    # ls.add(1)
    # print(ls.pop())

