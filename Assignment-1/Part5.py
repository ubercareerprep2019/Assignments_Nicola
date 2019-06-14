class TowerofHanoi:
    def __init__(self, fromRod, toRod, auxRod, n):
        self.fromRod = fromRod
        self.toRod = toRod
        self.auxRod = auxRod
        self.n = n
        self.moves = (2**n) - 1
        self.disks = []
        self.disks[fromRod] = n
        self.disks[toRod] = 0
        self.disks[auxRod] = 0
    def moveDisk(self, start, end):
        print("Move disk from ", start, "to ", end)

    def moveTower(self):
        for i in range(1, self.moves):
            if i%3 == 1:
                TowerofHanoi.moveDisk(self.fromRod, self.toRod)
                TowerofHanoi.disksAtRod(self.fromRod, self.toRod)
            elif i%3 == 2:
                TowerofHanoi.moveDisk(self.fromRod, self.auxRod)
                TowerofHanoi.disksAtRod(self.fromRod, self.auxRod)
            elif i%3 == 0:
                TowerofHanoi.moveDisk(self.auxRod, self.toRod)
                TowerofHanoi.disksAtRod(self.auxRod, self.toRod)

    def disksAtRod(self, rodindexfrom, rodindexto):
        self.disks[rodindexto] += 1
        self.disks[rodindexfrom] -= 1
        return self.disks
    
    
