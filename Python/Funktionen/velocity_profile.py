

class Trapezprofil_3_Stufen:
    
    def __init__(self, t1, t2, t3, v_max) -> None:
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.v_max = v_max
        self.a1 = v_max / t1
        self.a2 = -v_max / (t3 - t2)
        self.s1 = v_max * t1 / 2
        self.s2 = self.s1 + v_max * (t2 - t1)
        self.s3 = self.s2 + v_max * (t3 - t2) / 2
    
    def get_distance(self, t) -> float:
        
        s = -1
        if t < 0:
            print('t is out of range.')
        elif t < self.t1:
            s = 1/2 * self.a1 * t**2
        elif t < self.t2:
            s = self.s1 + self.v_max * (t - self.t1)
        elif t < self.t3:
            s = self.s2 + self.v_max * (t - self.t2) + 1/2 * self.a2 * (t - self.t2)**2
        else:
            print('t is out of range.')
        
        return s