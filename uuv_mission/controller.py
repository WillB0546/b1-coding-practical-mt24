class PDController:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.prev_error = None

    def reset(self):
        self.prev_error = None

    def __call__(self, reference: float, observation: float) -> float:
        e = float(reference) - float(observation)
        if self.prev_error is None:
            de = 0.0
        else:
            de = e - self.prev_error
        u = self.kp * e + self.kd * de
        self.prev_error = e
        return u