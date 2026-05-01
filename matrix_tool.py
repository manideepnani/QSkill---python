import numpy as np

# Better display format
np.set_printoptions(precision=2, suppress=True)


# -------------------- SAFE INPUT --------------------
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid integer.")


# -------------------- MATRIX INPUT --------------------
def input_matrix(name="Matrix"):
    print(f"\nEnter dimensions for {name}:")
    rows = get_int("Number of rows: ")
    cols = get_int("Number of columns: ")

    print(f"\nEnter elements for {name} row by row (space-separated):")
    matrix = []

    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i+1}: ").split()))
                if len(row) != cols:
                    print(f"❌ Please enter exactly {cols} values.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("❌ Please enter only numbers.")

    return np.array(matrix)


# -------------------- OPERATIONS --------------------
def add_matrices(a, b):
    return a + b

def subtract_matrices(a, b):
    return a - b

def multiply_matrices(a, b):
    return np.dot(a, b)

def transpose_matrix(a):
    return np.transpose(a)

def determinant_matrix(a):
    return np.linalg.det(a)

def scalar_multiply(a, k):
    return a * k


# -------------------- DISPLAY --------------------
def print_matrix(label, matrix):
    print(f"\n{label}:")
    print(matrix)


# -------------------- MAIN MENU --------------------
def main():
    while True:
        print("\n" + "="*45)
        print("   MATRIX OPERATIONS TOOL ")
        print("="*45)
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Transpose Matrix")
        print("5. Determinant of Matrix")
        print("6. Scalar Multiplication")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        # ---------- ADD ----------
        if choice == "1":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                print_matrix("Result (A + B)", add_matrices(A, B))
            else:
                print("❌ Error: Matrices must have same dimensions.")

        # ---------- SUBTRACT ----------
        elif choice == "2":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                print_matrix("Result (A - B)", subtract_matrices(A, B))
            else:
                print("❌ Error: Matrices must have same dimensions.")

        # ---------- MULTIPLY ----------
        elif choice == "3":
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape[1] == B.shape[0]:
                print_matrix("Result (A × B)", multiply_matrices(A, B))
            else:
                print("❌ Error: Columns of A must equal rows of B.")

        # ---------- TRANSPOSE ----------
        elif choice == "4":
            A = input_matrix("Matrix")
            print_matrix("Transpose", transpose_matrix(A))

        # ---------- DETERMINANT ----------
        elif choice == "5":
            A = input_matrix("Matrix")
            if A.shape[0] == A.shape[1]:
                det = determinant_matrix(A)
                print(f"\nDeterminant: {det:.2f}")
            else:
                print("❌ Error: Matrix must be square.")

        # ---------- SCALAR MULTIPLICATION ----------
        elif choice == "6":
            A = input_matrix("Matrix")
            k = float(input("Enter scalar value: "))
            print_matrix(f"Result ({k} × Matrix)", scalar_multiply(A, k))

        # ---------- EXIT ----------
        elif choice == "7":
            print("👋 Exiting program. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


# -------------------- RUN PROGRAM --------------------
if __name__ == "__main__":
    main()