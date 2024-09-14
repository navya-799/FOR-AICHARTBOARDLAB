def add(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])
def sub(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])
def mul(c1, c2):
    return (c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c2[0])
def conjugate(c):
    return (c[0], -c[1])
def print_complex(c):
    return f"{c[0]} + {c[1]}i"
if __name__ == "__main__":
    c1 = (4, 2)  
    
    c2 = (1, 5)  
    print(f"Complex Number 1: {print_complex(c1)}")
    print(f"Complex Number 2: {print_complex(c2)}")
    print(f"Addition: {print_complex(add(c1, c2))}")
    print(f"Subtraction: {print_complex(sub(c1, c2))}")
    print(f"Multiplication: {print_complex(mul(c1, c2))}")
    print(f"Conjugate of Complex Number 1: {print_complex(conjugate(c1))}")
    print(f"Conjugate of Complex Number 2: {print_complex(conjugate(c2))}")
