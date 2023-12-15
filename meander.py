import random
import re

class Meander:
    def __init__(self, lens_dict):
        self.lens_dict = lens_dict

    def process_lens_dictionary(self, meander_length):
        meander_length = meander_length % 10
        meander_length = int((meander_length / 10) * len(list(self.lens_dict.keys())))
        selected_keys = random.sample(list(self.lens_dict.keys()), meander_length)

        selected_dict = {}
        for key in selected_keys:
            if key in self.lens_dict:
                selected_dict[key] = self.lens_dict[key]
        
        return selected_dict

    
    def walk(self, meander_length):
        walk_elements = self.process_lens_dictionary(meander_length)
        walk = "["
        lag = 0
        for key,value in walk_elements.items():
            pattern = r'start(.*?)end'
            matches_srt = re.findall(pattern, key)
            pattern1 = r'(?<=end)(.*)'
            matches_end = re.findall(pattern1, key)
            dist = abs(int(matches_srt[0]) - lag)
            lag = int(matches_end[0]) 
    
            walk += f"={dist}=|"
            walk += f"{value}|"
        walk = walk.rstrip("|")  # Remove the trailing "|"
        walk += "]"
        return walk
    


if __name__ == "__main__":
    # import random
    # import string

    # # Function to generate a random word of a given length
    # def generate_random_word(length):
    #     letters = string.ascii_lowercase
    #     return ''.join(random.choice(letters) for _ in range(length))

    # # Sample lens dictionary with random words as values
    # lens_dict = {}
    # for i in range(1, 101):  # Assuming 100 entries
    #     key = f'lensIDTestLensstart{i}end{i + 1}'
    #     value = generate_random_word(random.randint(5, 10))  # Random word of length between 5 and 10
    #     lens_dict[key] = value

    # # Create a Meander instance with the populated dictionary
    # meander = Meander(lens_dict)

    # # Print selected values and walk through them as before
    # for meander_length in range(1, 11):
    #     meander.process_lens_dictionary(meander_length)

    # # Walk through selected values for a specific meander length (e.g., meander_length = 5)
    # print(meander.walk(5))
    pass
