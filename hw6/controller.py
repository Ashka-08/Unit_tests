from model import Model
from view import View

class Controller:

    def __init__(self, model=Model(), view=View()) -> None:
        self.model = model
        self.view = view
    
    def start(self):
        while(True):
            menu = self.view.menu()
            if menu == 1:
                self.model.arr1 = self.view.input_array()
                continue
            if menu == 2:
                self.model.arr2 = self.view.input_array()
                continue
            if menu == 3:
                self.view.out_text(self.model)
                continue
            if menu == 4:
                self.view.out_text(self.model.compare_averages())
                continue
            if menu == 0:
                self.view.out_text('Выход')
                exit()


if __name__ == "__main__":
    model = Model([1,2,3],[1,2,3])
    controller = Controller(model)

    # controller.view.out_text(model)
    controller.start()