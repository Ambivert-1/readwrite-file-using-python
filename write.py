
with open('dog_breeds.txt', 'r') as reader:
        dog_breeds = reader.readlines()

with open('dog_breeds_reversed.txt', 'w') as writer:
        for breed in reversed(dog_breeds):
            writer.write(breed)

print("Reversing and writing to 'dog_breeds_reversed.txt' successful.")


