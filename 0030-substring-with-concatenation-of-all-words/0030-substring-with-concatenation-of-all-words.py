from collections import Counter, defaultdict

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        window_len = word_len * total_words

        target = Counter(words)
        res = []

        # we try different starting offsets
        for offset in range(word_len):
            left = offset
            curr = defaultdict(int)
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target:
                    curr[word] += 1
                    count += 1

                    # shrink if too many of this word
                    while curr[word] > target[word]:
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1

                    # valid window
                    if count == total_words:
                        res.append(left)

                        # move left forward
                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    # reset window
                    curr.clear()
                    count = 0
                    left = right + word_len

        return res