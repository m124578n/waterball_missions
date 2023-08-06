from .State import State


class Teleport(State):
    def _set_name(self):
        self.name = "瞬身"

    def _set_time_limit(self):
        self.time_limit = 1

    def state_trigger(self):
        target = self.role.map.find_random_space()
        print(f"角色 {self.role.symbol} 被隨機移動到一個空地")
        self.role.map.move_object_to_target(self.role, target)
