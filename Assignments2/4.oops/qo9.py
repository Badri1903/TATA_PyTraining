#  class to reverse a string word by word

class Reverse:
    def reverse(self, s):
        return " ".join(reversed(s.split()))
r = Reverse()
s='I\'m Badri'
print(f'Reverse of {s}: {r.reverse(s)}')
