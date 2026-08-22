import pyjokes

# Print one random joke
joke = pyjokes.get_joke()
print("Joke of the moment:")
print(joke)

print()

# Print a few more jokes in a loop
print("Here are a few more:")
count = 1
while count <= 5:
    print(str(count) + ". " + pyjokes.get_joke())
    count = count + 1

print()

# A Chuck Norris style joke
print("Bonus Chuck Norris joke:")
print(pyjokes.get_joke(category="chuck"))