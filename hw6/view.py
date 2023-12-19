class View:
    def out_text(self, text:str) -> None:
        print(text)
    
    def input_text(self) -> str:
        text = input("Введите: \n")
        return text
    
    def print_menu(self) -> None:
        text_menu = "Выберите пункт меню цифрой: \n" \
            "1 - ввести первый массив, 2 - ввести второй массив,\n" \
            "3 - распечатать модель, 4 - сравнить массивы модели, 0 - выход"
        print(text_menu)
    
    def menu(self) -> int:
        while(True):
            self.print_menu()
            choise = self.input_text()
            try:
                choise = int(choise)
                if 0 <= choise <= 4:
                    return choise
                else:
                    print('Некорректный ввод: требуется цифра в диапазоне [0, 4]')
            except:
                print('Некорректный ввод: требуется цифра в диапазоне [0, 4]')
    
    def input_array(self) -> list[int]:
        while(True):
            res = []
            print("Введите числа через запятую")
            data = self.input_text()
            data = data.split(',')
            for el in data:
                try:
                    temp = int(el)
                    res.append(temp)
                except:
                    pass
            if len(data) == len(res):
                return res
            else:
                print('Ошибка ввода')
            

if __name__ == "__main__":
    v = View()
    v.out_text('Тест')
    print(v.menu())
    # print(v.input_array())


