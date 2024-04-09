from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        if year < 1900:
            self.year = 1900
        elif year > 2050:
            self.year = 1900
        else:
            self.year = year
        if month < 1:
            self.month = 1
        elif month > 12:
            self.month = 1
        else:
            self.month = month
        max_days = self.days_in_month(self.month, self.year)
        if day < 1:
            self.day = 1
        elif day > max_days:
            self.day = 1
        else:
            self.day = day

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        
    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        if month == 2:
            if Date.is_leap_year(year):
                return 29
            else:
                return 28
        elif month in {4, 6, 9, 11}:
            return 30
        else:
            return 31

    def get_delta_days(self,) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        dias = self.day - 1
        for x in range(1, self.month):
            dias += self.days_in_month(x, self.year)
        for y in range(1900, self.year):
            if self.is_leap_year(y):
                dias += 366
            else:
                dias += 365
        return dias
        

    @property
    def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        return (self.get_delta_days() + 1) % 7

    @property
    def is_weekend(self) -> bool:
        if self.weekday in {6, 0}:
            return True
        else:
            return False


    @property
    def short_date(self) -> str:
        '''02/09/2003'''
        if self.day >= 10:
            dia_str = str(self.day)
        else:
            dia_str = "0" + str(self.day)
        
        if self.month >= 10:
            month_str = str(self.month)
        else:
            month_str = "0" + str(self.month)
        
        return dia_str + "/" + month_str + "/" + str(self.year)

    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        dias_semana = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]
        dia_semana = dias_semana[self.weekday]
        nombres_month = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        nombre_month = nombres_month[self.month - 1]
        return f"{dia_semana.upper()} {self.day} DE {nombre_month.upper()} DE {self.year}"

    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        day = self.day + days
        month = self.month
        year = self.year
        while day > self.days_in_month(month, year):
            day -= self.days_in_month(month, year)
            month += 1
            if month > 12:
                month = 1
                year += 1
        return Date(day, month, year)

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        if isinstance(other, Date):
            return self.get_delta_days() - other.get_delta_days()

        elif isinstance(other, int):
            day = self.day - other
            month = self.month
            year = self.year
            
            while day < 1:
                month -= 1
                if month < 1:
                    month = 12
                    year -= 1
                day += self.days_in_month(month, year)
            
            return Date(day, month, year)
    def __lt__(self, other) -> bool:
        if self.day < other.day:
            return True
        if self.month < other.month:
            return True
        if self.year < other.year:
            return True
    def __gt__(self, other) -> bool:
        if self.day > other.day:
            return True
        if self.month > other.month:
            return True
        if self.year > other.year:
            return True

    def __eq__(self, other) -> bool:
        if self.day == other.day:
            return True
        if self.month == other.month:
            return True
        if self.year == other.year:
            return True