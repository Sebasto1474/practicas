class Employee:
    _base_salaries = {
    'trainee': 1000,
    'junior': 2000,
    'mid-level': 3000,
    'senior': 4000
}
    def __init__(self, name, level):
        if not isinstance(name, str) or not isinstance(level, str):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        if level not in Employee._base_salaries.keys():
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        self._name = name #utilizando _ por convencion para informar que estos atributos no deben ser modificados desde fuera de la clase.
        self._level = level
        self._salary = Employee._base_salaries[self._level]
    def __str__(self):
        return f"{self.name}: {self.level}"

# El método __repr__ es un método especial que se supone debe devolver una representación en cadena del objeto que pueda usarse para instanciarlo.
    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"
    
# El decorador @property se usa en Python para convertir un método en una propiedad. 
# Normalmente se usa para definir métodos getter, que son métodos usados para obtener el valor de un atributo:
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
    isinstance()

sebasto_king = Employee("Sebasto", "Petardo")
print(sebasto_king)
print(sebasto_king.name)
print(sebasto_king.level)
print(sebasto_king.__repr__())
print(repr(sebasto_king))