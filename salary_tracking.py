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

    @name.setter
    def name(self,new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self._name}'.")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if new_level not in Employee._base_salaries.keys():
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if new_level == self._level:
            raise ValueError(f"'{self._level}' is already the selected level.")
        if Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")
        print(f"'{self.name}' promoted to '{new_level}'.")
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, int) and not isinstance(new_salary, float):
            raise TypeError("'salary' must be a number.")
        if new_salary < self._salary:
            raise ValueError(f"Salary must be higher than minimum salary ${self._salary}.")
        self._salary = new_salary
        print(f"Salary updated to ${self._salary}.")

sebasto_king = Employee("Sebasto", "junior")
print(sebasto_king)
print(f"Base salary: {sebasto_king.salary}")
sebasto_king.level = "mid-level"