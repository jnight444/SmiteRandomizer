from old_code.src.object import Object


class Relic(Object):
    cooldown: int

    def __init__(self, name: str, cooldown: int, description: str):
        super(Relic, self).__init__(name, 0, description)
        self.cooldown = cooldown
