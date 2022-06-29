if __name__ == '__main__':
    len_square = int(input("Введите длину стороны квадрата: "))
    print("Периметр:", len_square * 4)
    print("Площадь:", len_square * len_square)
    print("")

    len_rectangle = int(input("Введите длину прямоугольника: "))
    width_rectangle = int(input("Введите ширину прямоугольника: "))
    print("Периметр:", (len_rectangle + width_rectangle) * 2)
    print("Площадь:", len_rectangle * width_rectangle)