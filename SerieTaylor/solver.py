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

        if variable == None and potencia == None:
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
        for i in range(len(self.monomio)):
            if monomio[i].isdigit() or monomio[i] == "-":
                self.coeficiente += str(monomio[i])
            if not(monomio[i].isdigit()) and monomio[i] != "-":
                try:
                    self.variable = self.monomio[i]
                except:
                    self.variable = ""
                try :
                    self.potencia = float(self.monomio[i+1: len(self.monomio)])
                except:
                    self.potencia = 1
                break

        try:
            self.coeficiente = float(self.coeficiente)
        except:
            self.coeficiente = -1.0

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
        return self.coeficiente * reemplazo ** self.potencia

    def Derivar(self):
        """
        Deriva el monomio
        :return: dato Monomio resultado de derivar funciones sencillas
        """
        return Monomio(self.coeficiente*self.potencia, self.variable, self.potencia - 1)

    def __str__(self):
        monomio = ""
        if self.coeficiente == -1.0 : monomio += "-"
        if self.coeficiente != 0.0:
            if self.coeficiente != 1.0 and self.coeficiente != -1.0:
                try:
                    monomio += str(int(self.coeficiente))
                except:
                    monomio += str(self.coeficiente)
            if self.potencia != 0:
                if(self.variable != ""): monomio += self.variable
                if self.potencia != 1:
                    try:
                        monomio += str(int(self.potencia))
                    except:
                        monomio += str(self.potencia)

        if monomio == "": monomio = "1"
        elif monomio == "-" : monomio = "-1"
        return monomio

class Polinomio:
    def __init__(self, polinomio : str):
        if polinomio.__contains__(" "): polinomio.replace(" ", "")
        polinomio = polinomio.replace("+", "_")
        polinomio = polinomio.replace("-", "_-")
        polinomio = polinomio.split("_")
        if polinomio.__contains__(''): polinomio.remove('')

        self.polinomio = []
        for monomio in polinomio:
            self.polinomio.append(Monomio(monomio))

    def __str__(self):
        polinomio = ""
        for monomio in self.polinomio:
            if monomio.coeficiente > 0:
                polinomio += " + " + str(monomio)
            elif monomio.coeficiente < 0:
                polinomio += " - " + str(monomio)[1:len(str(monomio))]
            else:
                pass

        if polinomio[1] == "+": polinomio = polinomio[3:len(str(polinomio))]

        return polinomio