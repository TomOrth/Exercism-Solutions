import random
import string
class Robot(object):
    def __init__(self):
        self.past_names = set()
        self.reset()
    def reset(self):
        temp = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
        if temp not in self.past_names:
            self.past_names.add(temp)
            self.name = temp
        else:
            self.reset()