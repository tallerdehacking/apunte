import random

class StreamCipher():

    def __init__(self):
        '''
        We make sure we are using all the bytes available,
        then, we shuffle them on each execution of the program.
        This way the generator will be very secure.
        '''
        self.bytes = [i for i in range(256)]
        self.i = -1
        random.shuffle(self.bytes)

    def next_byte(self):
        self.i = (self.i+1)%256
        return self.bytes[self.i]

    def next_bytes(self, num_bytes):
        return [self.next_byte() for i in range(num_bytes)]

    def encrypt(self, text):
        return bytearray([ord(text[i]) ^ self.next_byte() for i in range(len(text))])
