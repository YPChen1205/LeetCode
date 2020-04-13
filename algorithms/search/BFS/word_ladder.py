import collections
from collections import defaultdict


def ladder_length(begin_word, end_word, word_list):
    """
    :type begin_word: str
    :type end_word: str
    :type word_list: List[str]
    :rtype: int
    """

    if end_word not in word_list or not end_word or not begin_word or not word_list:
        return 0

    # all words are of same length.
    word_len = len(begin_word)

    all_combo_dict = defaultdict(list)

    for word in word_list:
        for i in range(word_len):
            all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

    queue = collections.deque([(begin_word, 1)])

    visited = {begin_word: True}  # make sure we don't repeat processing same word.
    while queue:
        current_word, level = queue.popleft()
        for i in range(word_len):
            intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

            # Next states are all the words which share the same intermediate state.
            for word in all_combo_dict[intermediate_word]:
                if word == end_word:
                    return level + 1
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            all_combo_dict[intermediate_word] = []
    return 0


if __name__ == '__main__':
    print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
