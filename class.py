class Car:
    class_name = "Car"

    def __init__(self):
        self.class_name  = None

    def show(self):
        print(self.class_name)

# Carクラスのインスタンスを作成します。
car = Car()

# Carの変数nameにセダンという文字列を格納します。
car.class_name = "セダン"

# Carのメソッドであるshow()を実行します。
car.show()