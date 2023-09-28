class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def evaluate_tree(root):
    if root is None:
        return 0

    if root.value == '+':
        return evaluate_tree(root.left) + evaluate_tree(root.right)
    elif root.value == '-':
        return evaluate_tree(root.left) - evaluate_tree(root.right)
    elif root.value == '*':
        return evaluate_tree(root.left) * evaluate_tree(root.right)
    elif root.value == '/':
        return evaluate_tree(root.left) / evaluate_tree(root.right)
    else:
        return float(root.value)  # jika node adalah angka

# Buat pohon aritmatika dengan contoh ekspresi: (7 + 6) * (9 - 5)
root = TreeNode('*')
root.left = TreeNode('+')
root.right = TreeNode('-')
root.left.left = TreeNode('7')
root.left.right = TreeNode('6')
root.right.left = TreeNode('9')
root.right.right = TreeNode('5')

# Evaluasi pohon aritmatika
hasil = evaluate_tree(root)
print("Hasil evaluasi ekspresi (7 + 6) * (9 - 5) adalah:", hasil)