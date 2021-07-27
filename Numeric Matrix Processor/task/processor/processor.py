import numpy as np


class MatrixProcessor:
    def __init__(self):
        self.size1 = None
        self.size2 = None
        self.matrix1 = []
        self.matrix2 = []
        self.show_menu()

    def show_menu(self):
        while True:
            self.matrix1 = []
            self.matrix2 = []
            print("1. Add matrices")
            print("2. Multiply matrix by a constant")
            print("3. Multiply matrices")
            print("4. Transpose matrix")
            print("5. Calculate a determinant")
            print("6. Inverse matrix")
            print("0. Exit")

            choice = int(input("Your choice: "))

            if choice == 1:
                self.get_matrices()
                self.add_matrices()
                print()
            elif choice == 2:
                self.scalar_multiplication()
                print()
            elif choice == 3:
                self.get_matrices()
                self.matrix_multiplication()
                print()
            elif choice == 4:
                self.transpose()
            elif choice == 5:
                self.determinant()
            elif choice == 6:
                self.inverse_matrix()
            elif choice == 0:
                return

    def get_matrices(self):
        self.size1 = list(map(int, input("Enter size of first matrix: ").split()))
        print("Enter first matrix:")
        for i in range(self.size1[0]):
            self.matrix1.append(list(map(float, input().split())))

        print("Enter second matrix:")
        self.size2 = list(map(int, input("Enter size of second matrix: ").split()))
        for i in range(self.size2[0]):
            self.matrix2.append(list(map(float, input().split())))

        self.matrix1 = np.asarray(self.matrix1)
        self.matrix2 = np.asarray(self.matrix2)

    def add_matrices(self):
        if self.size1 != self.size2:
            print("The operation cannot be performed.")
            return
        result = (self.matrix1 + self.matrix2).tolist()

        print("The result is:")
        [print(*line) for line in result]

    def scalar_multiplication(self):
        self.size1 = list(map(int, input("Enter size of matrix: ").split()))
        print("Enter matrix:")
        for i in range(self.size1[0]):
            self.matrix1.append(list(map(int, input().split())))

        self.matrix1 = np.asarray(self.matrix1)

        scalar = int(input("Enter constant: "))
        result = (self.matrix1 * scalar).tolist()

        print("The result is:")
        [print(*line) for line in result]

    def matrix_multiplication(self):
        if self.size1[1] != self.size2[0]:
            print("The operation cannot be performed.")
        else:
            result = (np.matmul(self.matrix1, self.matrix2)).tolist()

            print("The result is:")
            [print(*line) for line in result]

    def transpose(self):
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")

        choice = int(input())

        self.size1 = list(map(int, input("Enter matrix size: ").split()))
        print("Enter matrix:")
        for i in range(self.size1[0]):
            self.matrix1.append(list(map(float, input().split())))

        self.matrix1 = np.asarray(self.matrix1)

        if choice == 1:
            result = self.matrix1.T.tolist()
        elif choice == 2:
            result = np.flipud(np.fliplr(self.matrix1.T)).tolist()
        elif choice == 3:
            result = np.fliplr(self.matrix1).tolist()
        elif choice == 4:
            result = np.flipud(self.matrix1).tolist()

        print("The result is:")
        [print(*line) for line in result]

    def determinant(self):
        self.size1 = list(map(int, input("Enter matrix size: ").split()))
        print("Enter matrix:")
        for i in range(self.size1[0]):
            self.matrix1.append(list(map(float, input().split())))

        self.matrix1 = np.asarray(self.matrix1)

        result = np.linalg.det(self.matrix1).tolist()

        print("The result is:")
        print(result)

    def inverse_matrix(self):
        self.size1 = list(map(int, input("Enter matrix size: ").split()))
        print("Enter matrix:")
        for i in range(self.size1[0]):
            self.matrix1.append(list(map(float, input().split())))

        self.matrix1 = np.asarray(self.matrix1)

        try:
            result = np.linalg.inv(self.matrix1).tolist()

            print("The result is:")
            [print(*line) for line in result]
        except:
            print("This matrix doesn't have an inverse.")


_ = MatrixProcessor()
