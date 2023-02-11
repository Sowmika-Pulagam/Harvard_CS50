class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceeded")

        if n + self.size > self.capacity:
            raise ValueError("Exceeded capacity")
        self._size = self._size + n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("Withdraw the cookies")
        self._size = self._size - n

    @property #getter for capacity
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(4)
jar.withdraw(1)
print(jar)