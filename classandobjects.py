class Computer:

    def __init__(self,CPU,RAM):
        self.CPU = CPU
        self.RAM = RAM





    def config(self):
        print('Config is',self.CPU,'Cpu','and',self.RAM,'Ram')

com1 = Computer('i7',32)
com2 = Computer('Ryzen 7',16)



com1.config()
com2.config()