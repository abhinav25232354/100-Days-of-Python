# It doesn't belong to neither class not object(instance)
class Math:
    @staticmethod
    def add(a, b):
        return a + b

a = Math()
print(a.add(2, 4))