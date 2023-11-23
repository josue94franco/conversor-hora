class ConversorHora:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def convertir_a_palabras(self):
        horas = {
            1: 'una',
            2: 'dos',
            3: 'tres',
            4: 'cuatro',
            5: 'cinco',
            6: 'seis',
            7: 'siete',
            8: 'ocho',
            9: 'nueve',
            10: 'diez',
            11: 'once',
            12: 'doce'
        }

        minutos = {
            1: 'un minuto',
            2: 'dos minutos',
            3: 'tres minutos',
            4: 'cuatro minutos',
            5: 'cinco minutos',
            6: 'seis minutos',
            7: 'siete minutos',
            8: 'ocho minutos',
            9: 'nueve minutos',
            10: 'diez minutos',
            11: 'once minutos',
            12: 'doce minutos',
            13: 'trece minutos',
            14: 'catorce minutos',
            15: 'cuarto',
            16: 'dieciséis minutos',
            17: 'diecisiete minutos',
            18: 'dieciocho minutos',
            19: 'diecinueve minutos',
            20: 'veinte minutos',
            21: 'veintiún minutos',
            22: 'veintidós minutos',
            23: 'veintitrés minutos',
            24: 'veinticuatro minutos',
            25: 'veinticinco minutos',
            26: 'veintiséis minutos',
            27: 'veintisiete minutos',
            28: 'veintiocho minutos',
            29: 'veintinueve minutos',
            30: 'media'
        }
        
        if self.minuto == 0:
            return f'{horas[self.hora]} en punto'
        elif 1<=self.minuto <= 30:
            if self.minuto == 15:
                return f'{horas[self.hora]} y {minutos[self.minuto]}'
            else:
                return f'{horas[self.hora]} {minutos[self.minuto]} pasados'
        elif self.minuto > 30:
            if self.minuto == 45:
                return f'{horas[self.hora + 1]} menos cuarto'
            else:
                return f'{horas[self.hora +1]} menos {minutos[60 - self.minuto]}'
           
hora = int(input("Ingrese la hora: "))
minuto = int(input("Ingrese los minutos: "))

conversor = ConversorHora(hora, minuto)
resultado = conversor.convertir_a_palabras()
print(resultado)