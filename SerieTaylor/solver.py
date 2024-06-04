class Monomio:
    #monomio, coeficiente, variable, potencia
    def __init__(self, monomio_o_coeficiente:str|int|float,
                 variable:str = None, potencia : int | float = None):
        """
        Constructor de clase Monomio, acepta 1 o 3 parametros.
        :param monomio_o_coeficiente: Puede ser string para recibir directamente el monomio o bien, será el coeficiente
        unicamente
        :param variable: es el char que identifica la incognita
        :param potencia: es la potencia de la variable.
        """
        self.coeficiente = self.variable = ""
        self.potencia = 0

        if variable is None and potencia is None:
            self.__parse_from_string__(monomio_o_coeficiente)
        else:
            self.__parse_from_params__(monomio_o_coeficiente,
                                       variable, potencia)

    def __parse_from_string__(self, monomio : str):
        """
        Se supone que este método es inaccesible, por lo tanto no lo uses plox :3
        :param monomio:
        :return:
        """
        self.monomio = monomio.replace("^","")

        numero = True

        for i in range(len(self.monomio)):
            if not(monomio[i].isdigit()) and monomio[i] != '-' and monomio[i] != '.' and monomio[i] != ',':
                numero = False
                break

        if (not(numero)):
            for i in range(len(self.monomio)):
                if monomio[i].isdigit() or monomio[i] == '-' or monomio[i] == '.' or monomio[i] == ',':
                    self.coeficiente += str(monomio[i])
                if not(monomio[i].isdigit()) and monomio[i] != '-' and monomio[i] != '.' and monomio[i] != ',':
                    try:
                        self.variable = self.monomio[i]
                    except:
                        self.variable = ""
                    try :
                        self.potencia = float(self.monomio[i+1: len(self.monomio)])
                    except:
                        self.potencia = 1
                    break

            if self.coeficiente == "": self.coeficiente = 1
            else:
                try:
                    self.coeficiente = float(self.coeficiente)
                except:
                    self.coeficiente = 1
        else:
            self.coeficiente = float(self.monomio)

    def __parse_from_params__(self, coeficiente : int | float,
                              variable : str, potencia : int | float):
        """
        Se supone que este método es inaccesible, por lo tanto no lo uses plox :3
        :param coeficiente:
        :param variable:
        :param potencia:
        :return:
        """
        self.coeficiente = coeficiente
        self.variable = variable
        self.potencia = potencia

    def Reemplazar(self, reemplazo : float | int):
        """
        Reemplaza la incognita por el valor dado
        :param reemplazo: valor a reemplazar
        :return: dato float resultado de la operación
        """
        reg = self.coeficiente * reemplazo ** self.potencia
        if int(reg) == reg: return int(reg)
        else: return reg

    def Derivar(self):
        """
        Deriva el monomio
        :return: dato Monomio resultado de derivar funciones sencillas
        """
        if self.potencia !=0 :
            return Monomio(self.coeficiente*self.potencia, self.variable, self.potencia - 1)
        else:
            return Monomio("0")

    def __str__(self):
        monomio = ""
        if self.coeficiente != 0.0:
            if self.coeficiente != 1.0 and self.coeficiente != -1.0:
                if int(self.coeficiente) == self.coeficiente:
                    monomio += str(int(self.coeficiente))
                else:
                    monomio += str(self.coeficiente)
            elif self.coeficiente == -1.0: monomio += "-"
            if self.potencia != 0:
                if(self.variable != ""): monomio += self.variable
                if self.potencia != 1:
                    try:
                        monomio += "^" + str(int(self.potencia))
                    except:
                        monomio += "^" + str(self.potencia)
        else: return "";

        try:
            if self.coeficiente == 1 and monomio == '': monomio = "1"
            elif self.coeficiente == -1 and monomio == '-': monomio = "-1"
        except:
            pass
        finally:
            return monomio
class Polinomio:
    def __init__(self, polinomio : str):
        """
        Inicializa la clase polinomio
        :param polinomio: conjunto de monomios en dato string
        """
        if polinomio.__contains__("*"): polinomio = polinomio.replace('*','')
        if polinomio.__contains__(" "): polinomio = polinomio.replace(' ', '')
        polinomio = polinomio.replace("+", "_")
        polinomio = polinomio.replace("-", "_-")
        polinomio = polinomio.split("_")
        if polinomio.__contains__(''): polinomio.remove('')

        self.polinomio = []
        for monomio in polinomio:
            self.polinomio.append(Monomio(monomio))

    def Derivar(self):
        """
        Deriva el polinomio
        :return: un polinomio derivado en tipo str
        """
        derivada = ""
        for monomio in self.polinomio:
            d = monomio.Derivar()
            if d.coeficiente < 0: derivada += str(d)
            elif d.coeficiente > 0: derivada += "+"+str(d)
            else: pass

        return Polinomio(derivada)

    def Multiplicar(self, num : float | int, a : float | int):
        """
        Multiplica por el binomio num(x-a) donde:
        :param num: es el numero resultado del reemplazo respectivo
        :param a: es el numero inicial a buscar en y
        :return: Un binomio resultante de la multiplicación
        """
        new_a = num*a*-1
        if(new_a > 0): return Polinomio(str(num) + "x+" + str(new_a))
        elif(new_a < 0): return Polinomio(str(num) + "x" + str(new_a))
        else: return Polinomio(str(num) + "x")

    def Reemplazar(self, reemplazo: float | int):
        """
        Reemplaza todas las incognitas del polinomio por "reemplazo"
        :param reemplazo: el numero a reemplazar
        :return: dato float del resultado
        """
        res = 0.0
        for monomio in self.polinomio:
            res += monomio.Reemplazar(reemplazo)
        if int(res) == res: return int(res)
        else: return res

    def __str__(self):
        polinomio = ""
        for monomio in self.polinomio:
            if monomio.coeficiente > 0:
                polinomio += " + " + str(monomio)
            elif monomio.coeficiente < 0:
                polinomio += " - " + str(monomio)[1:len(str(monomio))]
            else:
                pass

        try:
            if polinomio[1] == "+": polinomio = polinomio[3:len(str(polinomio))]
        except:
            polinomio = "0"

        return polinomio