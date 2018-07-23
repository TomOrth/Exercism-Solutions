class SpaceAge(object):
    def __init__(self, seconds):
        self.merc = 0.2408467
        self.venu = 0.6151972
        self.mars = 1.8808158
        self.jupi = 11.862615
        self.satu = 29.447498
        self.uran = 84.016846
        self.nept = 164.79132
        self.earth_years = seconds/31557600
        self.seconds = seconds
    
    def on_mercury(self):
        return float('{:.2f}'.format(self.earth_years / self.merc))
    
    def on_venus(self):
        print(self.earth_years / self.venu)
        return float('{:.2f}'.format(self.earth_years / self.venu))

    def on_earth(self):
        return float('{:.2f}'.format(self.earth_years))
    
    def on_mars(self):
        return float('{:.2f}'.format(self.earth_years / self.mars))
    
    def on_jupiter(self):
        return float('{:.2f}'.format(self.earth_years / self.jupi))
    
    def on_saturn(self):
        return float('{:.2f}'.format(self.earth_years / self.satu))
    
    def on_uranus(self):
        return float('{:.2f}'.format(self.earth_years / self.uran))

    def on_neptune(self):
        return float('{:.2f}'.format(self.earth_years / self.nept))
