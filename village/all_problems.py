# import this
from collections import Counter

# ===== Variables and Some Arithmetic =====
a = 803
b = 993
print(f'{a}^2 + {b}^2 = {a**2 + b**2}')


# ===== Strings and Lists =====
wordOneStartPos = 44
wordOneEndPos = 48

wordTwoStartPos = 144
wordTwoEndPos = 153

txtStr = "VQPEb79EPdqryWuXKKzoba2phxSRDD0ScV1lMUqs25pJDipuscQ5rynwGNLmRXDNxtdaxlNqnH59DDjwdNZk8WyIvOZxehboofjzVUv4L5xFXZ5Ts18E4hDZRgzlxPSOeaASaXqhTcNB2xiablakistoniexMeNRf7KVM69AGkaTeuAJuQjq4fT3qF9AFaKv6EKz."

# Note: end position is not inclusive, so we add 1 to capture it
print(
    f'{txtStr[wordOneStartPos:wordOneEndPos + 1]} {txtStr[wordTwoStartPos:wordTwoEndPos + 1]}')


# ===== Conditions and Loops =====
startPos = 4309
endPos = 8902
result = 0

for x in range(startPos, endPos + 1):
    if x % 2 != 0:
        result += x

# result = sum(
#     [x for x in range(startPos, endPos + 1) if x % 2 != 0]
# )

print(result)


# ===== Working with Files =====
outputFile = []

with open('village/input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]


with open('village/out.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))


# ===== Dictionaries =====
txtStr = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# Generic approach:
wordCoutDict = {}

for word in txtStr.split(' '):
    if word in wordCoutDict:
        wordCoutDict[word] += 1
    else:
        wordCoutDict[word] = 1

# Optimized, Pythonic approach, using collections module:
# wordCoutDict = Counter(txtStr.split(' '))

for key, value in wordCoutDict.items():
    print(key, value)
