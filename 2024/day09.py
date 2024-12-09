from collections import deque
from tqdm import tqdm


class hard_drive:
    def __init__(self, file) -> None:
        with open(file) as f:
            data = [int(x) for x in f.read().strip()]
        self.mft = data
        self.drive = None
        self.fill()

    def fill(self):
        self.drive = deque(list() for _ in self.mft)
        index = 0
        is_file = True
        for i in range(len(self.mft)):
            if is_file:
                for _ in range(self.mft[i]):
                    self.drive[i].append(index)
                index += 1
                is_file = False
            else:
                for _ in range(self.mft[i]):
                    self.drive[i].append(-1)
                is_file = True

    def checksum(self) -> int:
        i = 0
        checksum = 0
        for point in self.drive:
            if point >= 0:
                checksum += point * i
            i += 1
        return checksum

    def free_space(self) -> None:
        compact = deque()
        while len(self.drive) > 0:
            sector = self.drive.popleft()
            is_file = len(sector) > 0 and sector[0] > -1
            if is_file:
                for s in sector:
                    compact.append(s)
                is_file = False
            else:
                if len(self.drive) > 0:
                    target = self.drive.pop()
                if len(sector) < len(target):
                    for _ in range(len(sector)):
                        compact.append(target.pop())
                    self.drive.append(target)
                elif len(sector) == len(target):
                    for _ in range(len(sector)):
                        compact.append(target.pop())
                    self.drive.pop()  # Remove space
                else:
                    for _ in range(len(target)):
                        compact.append(target.pop())
                        sector.pop()
                    self.drive.appendleft(sector)
                    self.drive.pop()  # Remove space
        self.drive = compact

    def defragment(self) -> None:
        for i in tqdm(
            range(len(self.drive) - 1, -1, -2)
        ):  # Start from last block, skip free blocks
            for j in range(1, i, 2):  # Only check potential free space
                if (
                    len(self.drive[j]) > 0 and self.drive[j][-1] == -1
                ):  # Find the leftmost block with empty space
                    free_space = sum(1 for x in self.drive[j] if x == -1)
                    freed = len(self.drive[i])
                    if freed <= free_space:
                        dr = []
                        for k in range(len(self.drive[j])):
                            if self.drive[j][k] == -1 and len(self.drive[i]) > 0:
                                dr.append(self.drive[i].pop())
                            else:
                                dr.append(self.drive[j][k])
                        self.drive[j] = dr
                        self.drive[i] = [-1 for _ in range(freed)]
                        break

        defrag = deque()
        for sector in self.drive:
            for s in sector:
                defrag.append(s)
        self.drive = defrag


hd = hard_drive("2024/input/day09")

hd.free_space()
print("Part 1:", hd.checksum())

hd.fill()

hd.defragment()
print("Part 2:", hd.checksum())
