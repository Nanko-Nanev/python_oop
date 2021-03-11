class ExercisePlan:
    exercise_plan_count = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        ExercisePlan.exercise_plan_count += 1
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.exercise_plan_count

    @classmethod
    def from_hours(cls, trainer_id, equipment_id, hours):
        return cls(trainer_id, equipment_id, hours * 60)

    @classmethod
    def get_next_id(cls):
        return cls.exercise_plan_count + 1

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"