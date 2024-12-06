# Initialize counting variables
A_count = 0
B_count = 0
C_count = 0
D_count = 0
E_count = 0
F_count = 0
G_count = 0
H_count = 0
I_count = 0
J_count = 0
K_count = 0
L_count = 0
M_count = 0
N_count = 0
O_count = 0
P_count = 0
Q_count = 0
R_count = 0
S_count = 0
T_count = 0
U_count = 0
V_count = 0
W_count = 0
X_count = 0
Y_count = 0
Z_count = 0

# Open the file for reading
with open('declaration.text', 'r') as f:
    # Read in content of the entire file
    content = f.read()
    # Uppercase the content
    content = content.upper()
    # Count each character A-Z
    for ch in content:
        match ch:
            case 'A': A_count += 1
            case 'B': B_count += 1
            case 'C': C_count += 1
            case 'D': D_count += 1
            case 'E': E_count += 1
            case 'F': F_count += 1
            case 'G': G_count += 1
            case 'H': H_count += 1
            case 'I': I_count += 1
            case 'J': J_count += 1
            case 'K': K_count += 1
            case 'L': L_count += 1
            case 'M': M_count += 1
            case 'N': N_count += 1
            case 'O': O_count += 1
            case 'P': P_count += 1
            case 'Q': Q_count += 1
            case 'R': R_count += 1
            case 'S': S_count += 1
            case 'T': T_count += 1
            case 'U': U_count += 1
            case 'V': V_count += 1
            case 'W': W_count += 1
            case 'X': X_count += 1
            case 'Y': Y_count += 1
            case 'Z': Z_count += 1

    # Report the counts for each letter
    print('A: ', A_count)
    print('B: ', B_count)
    print('C: ', C_count)
    print('D: ', D_count)
    print('E: ', E_count)
    print('F: ', F_count)
    print('G: ', G_count)
    print('H: ', H_count)
    print('I: ', I_count)
    print('J: ', J_count)
    print('K: ', K_count)
    print('L: ', L_count)
    print('M: ', M_count)
    print('N: ', N_count)
    print('O: ', O_count)
    print('P: ', P_count)
    print('Q: ', Q_count)
    print('R: ', R_count)
    print('S: ', S_count)
    print('T: ', T_count)
    print('U: ', U_count)
    print('V: ', V_count)
    print('W: ', W_count)
    print('X: ', X_count)
    print('Y: ', Y_count)
    print('Z: ', Z_count)

