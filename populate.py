import random
import string

class Populate:
    def __init__(self, lens_dict):
        self.lens_dict = lens_dict

    # Function to generate a random word of a given length
    @staticmethod
    def generate_random_word(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def generate_random_lens_dict(self):
        for key in self.lens_dict.keys():
            value = self.generate_random_word(random.randint(5, 10))
            self.lens_dict[key] = value
        
        return self.lens_dict

    def user_populate_lens_dict(self):
        for key in self.lens_dict.keys():
            value = input(f"Enter a value for key '{key}': ")
            self.lens_dict[key] = value
        
        return self.lens_dict

if __name__ == "__main__":
    # lens_dict = {
    #     'key1': '',
    #     'key2': '',
    #     'key3': ''
    # }

    # populator = Populate(lens_dict)

    # # Automatically generate random values
    # populator.generate_random_lens_dict()

    # # Allow the user to populate values
    # populator.user_populate_lens_dict()

    # # Print the populated dictionary
    # print(lens_dict)
    pass
