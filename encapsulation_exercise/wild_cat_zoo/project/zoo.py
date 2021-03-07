class Zoo:
    def __init__(self, name, budget, animlal_capacity, workers_capacity):
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_salary = sum([worker.salary for worker in self.workers])
        if self.__budget < sum_salary:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= sum_salary
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        money_needed = sum([animal.get_needs() for animal in self.animals])
        if self.__budget < money_needed:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= money_needed
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    # def animals_status(self):
    #     print(f"You have {len(self.animals)} animals")
    #     lions = [lion for lion in self.animals if lion.__class__.__name__ == "Lion"]
    #     tigers = [tiger for tiger in self.animals if tiger.__class__.__name__ == "Tiger"]
    #     cheetah = [cheetah for cheetah in self.animals if cheetah.__class__.__name__ == "Cheetah"]
    #
    #     print(f"----- {len(lions)} Lions:")
    #     for lion in lions:
    #         print(lion.__repr__())
    #     print(f"----- {len(tigers)} Tigers:")
    #     for tiger in tigers:
    #         print(tiger.__repr__())
    #     print(f"----- {len(cheetah)} Cheetahs:")
    #     for cheet in cheetah:
    #         print(cheet.__repr__())
    def animals_status(self):
        l = [l for l in self.animals if l.__class__.__name__ == 'Lion']
        t = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
        c = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']
        result = f'You have {len(self.animals)} animals\n'
        result += f'----- {len(l)} Lions:\n'
        result += '\n'.join([x.__repr__() for x in l]) + '\n'
        result += f'----- {len(t)} Tigers:\n'
        result += '\n'.join([x.__repr__() for x in t]) + '\n'
        result += f'----- {len(c)} Cheetahs:\n'
        result += '\n'.join([x.__repr__() for x in c])
        return result

    # def animals_status(self):
    #     l = [l for l in self.animals if l.__class__.__name__ == 'Lion']
    #     t = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
    #     c = [c for c in self.animals if c.__class__.__name__ == 'Cheetah']
    #     result = f'You have {len(self.animals)} animals\n'
    #     result += f'----- {len(l)} Lions:\n'
    #     result += '\n'.join([x.__repr__() for x in l]) + '\n'
    #     result += f'----- {len(t)} Tigers:\n'
    #     result += '\n'.join([x.__repr__() for x in t]) + '\n'
    #     result += f'----- {len(c)} Cheetahs:\n'
    #     result += '\n'.join([x.__repr__() for x in c])
    #     return result

    # def workers_status(self):
    #     keepers = [keeper for keeper in self.workers if keeper.__class__.__name__ == "Keeper"]
    #     caretakers = [care for care in self.workers if care.__class__.__name__ == "Caretakers"]
    #     vets = [vet for vet in self.workers if vet.__class__.__name__ == "Vets"]
    #     print(f"You have {len(self.workers)} workers")
    #     print(f"----- {len(keepers)} Keepers:")
    #     for keeper in keepers:
    #         print(keeper.__repr__())
    #     print(f"----- {len(caretakers)} Caretakers:")
    #     for care in caretakers:
    #         print(care.__repr__())
    #     print(f"----- {len(vets)} Vets:")
    #     for vet in vets:
    #         print(vet.__repr__())
    def workers_status(self):
        k = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        c = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        v = [v for v in self.workers if v.__class__.__name__ == 'Vet']
        result = f'You have {len(self.workers)} workers\n'
        result += f'----- {len(k)} Keepers:\n'
        result += '\n'.join([x.__repr__() for x in k]) + '\n'
        result += f'----- {len(c)} Caretakers:\n'
        result += '\n'.join([x.__repr__() for x in c]) + '\n'
        result += f'----- {len(v)} Vets:\n'
        result += '\n'.join([x.__repr__() for x in v])
        return result


