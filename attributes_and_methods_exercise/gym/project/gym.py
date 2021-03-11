class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if not customer in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not plan in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not subscription in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):

        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]
        customer = [c for c in self.customers if c.id == subscription.customer_id][0]
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
        plan = [p for p in self.plans if p.id == trainer.id][0]
        equipment = [e for e in self.equipment if e.id == plan.id][0]

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"

# def subscription_info(self,subscription_id):
# subscription = [s for s in self.subscriptions if s.id ==  subscription_id][0]
# customer_id = subscription.customer_id
# customer = [c for c in self.customers if c.id == customer_id][0]
# trainer_id = subscription.trainer_id
# trainer = [t for t in self.trainers if t.id == trainer_id][0]
# plan_id = subscription.exercise_id
# plan = [p for p in self.plans if p.id == plan_id][0]
# equipment_id = plan.equipment_id
# equipment = [e for e in self.equipment if e.id == equipment_id][0]

# result = subscription.__repr__() + "\n"
# result += customer.__repr__() + "\n"
# result += trainer.__repr__() + "\n"
# result += equipment.__repr__() + "\n"
# result += plan.__repr__()
# return  result