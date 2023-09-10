class StableMarriage:
    def __init__(self, n):
        self.people = n
        self.males = []
        self.females = []

    def read_input(self, filename):
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            for _ in range(n):
                row = list(map(int, file.readline().strip().split()))
                self.males.append(row)

            for _ in range(n):
                row = list(map(int, file.readline().strip().split()))
                self.females.append(row)

    def print(self):
        print("The 2D array is:")
        for row in self.males:
            print(row)

        # Print the 2D array
        print("\n\nThe 2D array is:")
        for row in self.females:
            print(row)

    def returnPairs(self):
        pairs = set()


        return pairs
    
    def propose(self):
        pass

    def accept_deny(self):
        pass

    def choiceBetter(self):
        pass








# Example usage:
sm = StableMarriage(6)
sm.read_input('input.txt')
sm.print()

