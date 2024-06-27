d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'

try:
    with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
        # Read all lines from the file into a list
        dog_breeds = reader.readlines()

        # Write reversed lines to the output file
        writer.writelines(reversed(dog_breeds))

    print(f"Successfully reversed and wrote to '{d_r_path}'.")

except IOError as e:
    print(f"Error: {e}")
