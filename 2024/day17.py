class TBComputer:
    def __init__(self, file) -> None:
        with open(file) as f:
            data = f.read().splitlines()

        self.A = int(data[0].split(": ")[1])
        self.B = int(data[1].split(": ")[1])
        self.C = int(data[2].split(": ")[1])
        self.instructions = [int(x) for x in data[4].split(": ")[-1].split(",")]
        self.pointer = 0
        self.buffer = []
        self.reference = "".join(str(x) for x in self.instructions)

    def combo(self, operand):
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.A
            case 5:
                return self.B
            case 6:
                return self.C
            case 7:
                print("Error: Invalid Operand")

    def adv(self, operand):
        self.A = self.A >> self.combo(operand)  # // (2**self.combo(operand))
        self.pointer += 2

    def bxl(self, operand):
        self.B = self.B ^ operand
        self.pointer += 2

    def bst(self, operand):
        self.B = self.combo(operand) % 8
        self.pointer += 2

    def jnz(self, operand):
        if self.A != 0:
            self.pointer = operand
        else:
            self.pointer += 2

    def bxc(self, _):
        self.B = self.B ^ self.C
        self.pointer += 2

    def out(self, operand):
        self.buffer.append(self.combo(operand) % 8)
        self.pointer += 2

    def bdv(self, operand):
        self.B = self.A >> self.combo(operand)
        self.pointer += 2

    def cdv(self, operand):
        self.C = self.A >> self.combo(operand)
        self.pointer += 2

    def process(self):
        while self.pointer < len(self.instructions):
            instruction = self.instructions[self.pointer]
            operand = self.instructions[self.pointer + 1]
            match instruction:
                case 0:
                    self.adv(operand)
                case 1:
                    self.bxl(operand)
                case 2:
                    self.bst(operand)
                case 3:
                    self.jnz(operand)
                case 4:
                    self.bxc(operand)
                case 5:
                    self.out(operand)
                case 6:
                    self.bdv(operand)
                case 7:
                    self.cdv(operand)

    def write_buffer(self):
        return ",".join(str(x) for x in self.buffer)

    def solve(self, i=0, fixed=""):
        if len(fixed) < 48:
            for b in ["000", "001", "010", "011", "100", "101", "110", "111"]:
                s = fixed[:]
                s += b
                s += "".join("1" for _ in range(48 - len(s)))
                n = int(s, 2)
                A = n
                result = ""
                while A > 0:
                    B = A % 8
                    B = B ^ 7
                    C = A >> B
                    B = B ^ C
                    B = B ^ 4
                    result += str(B % 8)
                    A = A >> 3
                if result == self.reference:
                    return int(s, 2)
                if result[-(1 + i)] == self.reference[-(1 + i)]:
                    x = self.solve(i + 1, fixed[:] + b[:])
                    if x is not None:
                        return x
        return None

    def __str__(self):
        s = f"""Registers: {self.A}, {self.B}, {self.C}
        Pointer: {self.pointer}
        Instructions: {self.instructions}
        """
        return s


input = "2024/input/day17"
computer = TBComputer(input)

computer.process()
print("Part 1:", computer.write_buffer())
print("Part 2:", computer.solve())
