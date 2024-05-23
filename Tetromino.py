class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.rotation_index = 0
        self.rotations = self.generate_rotations(shape)
    
    def generate_rotations(self, shape):
        rotations = [shape]
        for _ in range(3):
            shape = self.rotate_90_degrees(shape)
            rotations.append(shape)
        return rotations
    
    def rotate_90_degrees(self, shape):
        return [list(row) for row in zip(*shape[::-1])]
    
    def rotate(self):
        self.rotation_index = (self.rotation_index + 1) % 4
        self.shape = self.rotations[self.rotation_index]
    
    def __str__(self):
        return '\n'.join(''.join(row) for row in self.shape)
    
    def __eq__(self, other):
        return self.shape == other.shape
    
    def is_similar(self, other):
        return any(self.shape == rotation for rotation in other.rotations)

# Definir los tetrominós
tetrominos = {
    'I': [['.', '.', '.', '.'],
          ['@', '@', '@', '@'],
          ['.', '.', '.', '.'],
          ['.', '.', '.', '.']],
    
    'O': [['@', '@'],
          ['@', '@']],
    
    'T': [['.', '@', '.'],
          ['@', '@', '@'],
          ['.', '.', '.']],
    
    'S': [['.', '@', '@'],
          ['@', '@', '.'],
          ['.', '.', '.']],
    
    'Z': [['@', '@', '.'],
          ['.', '@', '@'],
          ['.', '.', '.']],
    
    'J': [['@', '.', '.'],
          ['@', '@', '@'],
          ['.', '.', '.']],
    
    'L': [['.', '.', '@'],
          ['@', '@', '@'],
          ['.', '.', '.']],
}

# Función para imprimir tetrominó
def print_tetromino(tetromino):
    print(tetromino)
    print()

# Crear instancia del tetrominó 'T' y rotarlo
tetromino_t = Tetromino(tetrominos['T'])
print("T en su estado original:")
print_tetromino(tetromino_t)

tetromino_t.rotate()
print("T después de una rotación:")
print_tetromino(tetromino_t)

tetromino_t.rotate()
print("T después de dos rotaciones:")
print_tetromino(tetromino_t)

# Crear dos instancias de tetrominós
tetromino_z1 = Tetromino(tetrominos['Z'])
tetromino_z2 = Tetromino(tetrominos['Z'])

# Comparar igualdad
print("Comparar igualdad:")
print(tetromino_z1 == tetromino_z2)

# Comparar semejanza
tetromino_z2.rotate()
print("Comparar semejanza después de una rotación:")
print(tetromino_z1.is_similar(tetromino_z2))

# Pruebas unitarias
import unittest

class TestTetromino(unittest.TestCase):
    def test_rotation(self):
        tetromino = Tetromino(tetrominos['T'])
        tetromino.rotate()
        expected = [['@', '.', '.'],
                    ['@', '@', '.'],
                    ['@', '.', '.']]
        self.assertEqual(tetromino.shape, expected)
    
    def test_equality(self):
        tetromino1 = Tetromino(tetrominos['Z'])
        tetromino2 = Tetromino(tetrominos['Z'])
        self.assertEqual(tetromino1, tetromino2)
    
    def test_similarity(self):
        tetromino1 = Tetromino(tetrominos['Z'])
        tetromino2 = Tetromino(tetrominos['Z'])
        tetromino2.rotate()
        self.assertTrue(tetromino1.is_similar(tetromino2))

if __name__ == '__main__':
    unittest.main()
