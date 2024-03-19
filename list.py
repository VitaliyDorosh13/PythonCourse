superPowers = ['flight', 'cool cape', '20/20 vision', 'Coding Skilz']
superWeaknesses = ['bolonga', 'lactose intolerance', 'social settings', 'tight trunks']

print(superPowers)

print(superPowers[3])

del superWeaknesses[1]
print(*superWeaknesses)     #superWeaknesses.remove('lactose intolerance')
superWeaknesses.append('taco meat')
print(*superWeaknesses)

superWeaknesses.insert(1, 'Sneeze')
print(*superWeaknesses)

superWeaknesses.pop(1)
print(*superWeaknesses)

superWeaknesses.reverse()
print(*superWeaknesses)

superWeaknesses.sort()
print(*superWeaknesses)

print(superWeaknesses.count('social settings'))

#superWeaknesses.extend(moreSuperWeaknesses)

superWeaknesses2 = superWeaknesses.copy()

print(superWeaknesses.index("taco meat"))

superWeaknesses2.clear()
print(*superWeaknesses2)
'''
print(superPowers[0], "is located at index 0")
print(superPowers[1], "is located at index 1")
print(superPowers[2], "is located at index 2")
print(superPowers[3], "is located at index 3")

print("Belong our fledgling hero/sidekick, \"Wonder Boy")
print("His super power include:", *superPowers)
print("And his weaknesses are:", *superWeaknesses)
'''