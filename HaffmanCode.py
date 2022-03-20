from collections import Counter


class Node:
    def __init__(self, character, probability, left, right):
        self.character = character
        self.probability = probability
        self.left = left
        self.right = right


text = input("Enter Text: ")
text = text.replace(" ", "")

characterFreq = Counter(text)
print(characterFreq)
charWithProbability = []

for i in characterFreq:
    charWithProbability.append(Node(i, characterFreq[i] / len(text), None, None))

while len(charWithProbability) != 1:
    charWithProbability.sort(key=lambda x: x.probability)
    left = charWithProbability.pop(0)
    right = charWithProbability.pop(0)
    charWithProbability.append(Node(
        left.character + right.character,
        left.probability + right.probability,
        left, right
    ))
print(Counter(charWithProbability))
print(charWithProbability[0].character, charWithProbability[0].probability)


def travel(local_node, code):
    if local_node.left is None and local_node.right is None:
        print(f"{local_node.character} -> {code}")
    if local_node.left is not None:
        travel(local_node.left, code + "0")
    if local_node.right is not None:
        travel(local_node.right, code + "1")


travel(charWithProbability[0], "")
