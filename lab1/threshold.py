import math

class Perceptrone:

    def __init__(self):
        self.weights = [0, 0, 0, 0, 0]

    def activation_func(self, net):
        if net < 0:
            return 0
        else:
            return 1

    def study(self, norma):

        table = [[0, 0, 0, 0, 1],
                 [0, 0, 0, 1, 1],
                 [0, 0, 1, 0, 1],
                 [0, 0, 1, 1, 1],
                 [0, 1, 0, 0, 1],
                 [0, 1, 0, 1, 1],
                 [0, 1, 1, 0, 1],
                 [0, 1, 1, 1, 1],
                 [1, 0, 0, 0, 1],
                 [1, 0, 0, 1, 1],
                 [1, 0, 1, 0, 1],
                 [1, 0, 1, 1, 1],
                 [1, 1, 0, 0, 1],
                 [1, 1, 0, 1, 1],
                 [1, 1, 1, 0, 1],
                 [1, 1, 1, 1, 1]]

        answers = [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]

        error = 0

        weight_update = self.weights.copy()

        for k in range(len(table)):
            net = 0
            for i in range(len(table[k])):
                net += table[k][i] * weight_update[i]

            mistake = answers[k] - self.activation_func(net)
            if mistake != 0:
                error += 1

            for i in range(len(weight_update)):
                weight_update[i] += norma * mistake * table[k][i]

        self.weights = weight_update.copy()
        print(self.weights)


        return error

    def run(self, vector):

        net = 0
        for i in range(len(vector) - 1):
            net += vector[i] * self.weights[i]
        net += self.weights[len(self.weights) - 1]

        return self.activation_func(net)


if __name__ == '__main__':

    neuronet = Perceptrone()

    k = 0

    errors = []

    error = neuronet.study(0.2)
    print(neuronet.run([0, 0, 0, 0, 1]))
    print(neuronet.run([0, 0, 0, 1, 1]))
    print(neuronet.run([0, 0, 1, 0, 1]))
    print(neuronet.run([0, 0, 1, 1, 1]))
    print(neuronet.run([0, 0, 1, 1, 1]))
    print(neuronet.run([0, 1, 0, 1, 1]))
    print(neuronet.run([0, 1, 1, 0, 1]))
    print(neuronet.run([0, 1, 1, 1, 1]))
    print(neuronet.run([1, 0, 0, 0, 1]))
    print(neuronet.run([1, 0, 0, 1, 1]))
    print(neuronet.run([1, 0, 1, 0, 1]))
    print(neuronet.run([1, 0, 1, 1, 1]))
    print(neuronet.run([1, 1, 0, 0, 1]))
    print(neuronet.run([1, 1, 0, 1, 1]))
    print(neuronet.run([1, 1, 1, 0, 1]))
    print(neuronet.run([1, 1, 1, 1, 1]))

    while (error != 0):
        errors.append(error)
        error = neuronet.study(0.3)
        print(neuronet.run([0, 0, 0, 0, 1]))
        print(neuronet.run([0, 0, 0, 1, 1]))
        print(neuronet.run([0, 0, 1, 0, 1]))
        print(neuronet.run([0, 0, 1, 1, 1]))
        print(neuronet.run([0, 0, 1, 1, 1]))
        print(neuronet.run([0, 1, 0, 1, 1]))
        print(neuronet.run([0, 1, 1, 0, 1]))
        print(neuronet.run([0, 1, 1, 1, 1]))
        print(neuronet.run([1, 0, 0, 0, 1]))
        print(neuronet.run([1, 0, 0, 1, 1]))
        print(neuronet.run([1, 0, 1, 0, 1]))
        print(neuronet.run([1, 0, 1, 1, 1]))
        print(neuronet.run([1, 1, 0, 0, 1]))
        print(neuronet.run([1, 1, 0, 1, 1]))
        print(neuronet.run([1, 1, 1, 0, 1]))
        print(neuronet.run([1, 1, 1, 1, 1]))
        k += 1

    # plt.plot(errors)
    # plt.xlabel('Номер эпохи')
    # plt.ylabel('Количество ошибок')
    # plt.title('Пороговая функция на полной выборке')
    # plt.grid()
    # plt.show()

    print(k)
    print('\n')
