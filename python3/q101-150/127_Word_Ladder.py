from typing import List
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        chars = 'abcdefghijklmnopqrstuvwxyz'

        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in chars:
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordList:
                        wordList.remove(newWord)
                        queue.append((newWord, length+1))

        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]

    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, wordList))
