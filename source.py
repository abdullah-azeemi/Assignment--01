class StableMarriage:
    def __init__(self, n):
        self.n = n
        self.male_preferences = {} 
        self.female_preferences = {}  
        self.femalesEngaged = {}  
        self.malesEngaged = {}  
        self.male_proposals = {}  

    def read_input(self, filename):
        with open(filename, 'r') as file:
            n = int(file.readline().strip())

            for _ in range(n):
                row = list(map(int, file.readline().strip().split()))
                male = row[0]
                preferences = row[1:]
                self.male_preferences[male] = preferences
                self.malesEngaged[male] = None
                self.male_proposals[male] = 0

            for _ in range(n):
                row = list(map(int, file.readline().strip().split()))
                female = row[0]
                preferences = row[1:]
                self.female_preferences[female] = preferences
                self.femalesEngaged[female] = None

    def gale_shapley(self):
        while None in self.malesEngaged.values():  
            for male in self.malesEngaged.keys():
                if self.malesEngaged[male] is None:
                    female = self.male_preferences[male][self.male_proposals[male]]
                    current_male = self.femalesEngaged[female]

                    if current_male is None:
                    
                        self.malesEngaged[male] = female
                        self.femalesEngaged[female] = male
                    else:
                    
                        if self.female_preferences[female].index(male) < self.female_preferences[female].index(current_male):
                            self.malesEngaged[male] = female
                            self.femalesEngaged[female] = male
                            self.malesEngaged[current_male] = None
                    self.male_proposals[male] += 1

    def print_matches(self):
        for female, male in self.femalesEngaged.items():
            print(f'Male {male} : Female {female}')


if __name__ == "__main__":
    n = 6  
    marriage = StableMarriage(n)
    marriage.read_input("input.txt")  

    marriage.gale_shapley()
    marriage.print_matches()
