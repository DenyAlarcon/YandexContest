# Реализовать стек с возможность получения суммы n первых элементов за O(1).

class stack(object):
    def __init__(self):
        self.values = []
        self.sums = [0]

    def push(self, value):
        self.values.append(value)
        if len(self.sums) > 0:
            self.sums.append(self.sums[-1] + value)

    def pop(self):
        if len(self.sums) > 0:
            self.sums.pop()
            return self.values.pop()

    def get_sum(self, n):
        if n > -1 and n < len(self.sums):
            return self.sums[n]


def main():
    st = stack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.get_sum(1))
    print(st.get_sum(2))
    print(st.get_sum(3))
    st.pop()
    print(st.get_sum(1))
    print(st.get_sum(2))
    print(st.get_sum(3))


if __name__ == "__main__":
    main()
