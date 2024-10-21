import pytest
from ajedrezoo import metapieza, ocupadas, cocupadas

def limpiar_matriz():
    for i in range(9):
        for j in range(9):
            cocupadas[i][j] = 0

class TestMetapiezaInit:

    def test_case_1(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)

        #Postcondición:
        assert ob1.movdiagonal(1) == [(3, 3), (5, 5), (5, 3), (3, 5)]

    def test_case_2(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)
        ob2 = metapieza(5, 3, 2)

        #Postcondición:
        assert ob1.movdiagonal(1) == [(3, 3), (5, 5), (3, 5)]

    def test_case_3(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)
        ob2 = metapieza(5, 3, 2)

        #Postcondición:
        assert ob1.movdiagonal(2) == [(3, 3), (5, 5), (3, 5), (2, 2), (6, 6), (2, 6)]

    def test_case_4_y_15(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(1, 4, 2)

        #Postcondición:
        assert ob1.movdiagonal(1) == [(2, 5), (2, 3)]

    def test_case_5_y_13(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 8, 2)

        #Postcondición:
        assert ob1.movdiagonal(1) == [(3, 7), (5, 7)]

    def test_case_6(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)
        ob2 = metapieza(3, 5, 2)

        #Postcondición:
        assert ob1.movdiagonal(1) == [(3, 3), (5, 5), (5, 3)]

    def test_case_7(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)
        ob2 = metapieza(3, 5, 2)

        #Postcondición:
        assert ob1.movdiagonal(2) == [(3, 3), (5, 5), (5, 3), (2, 2), (6, 6), (6, 2)]

    def test_case_8_y_12(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(8, 4, 2)

        #Postcondición:
        assert ob1.movdiagonal(1) == [(7, 3), (7, 5)]

    def test_case_9_y_17(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 1, 2)

        #Postcondición:
        assert ob1.movdiagonal(1) == [(5, 2), (3, 2)]
        
    def test_case_10(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)
        ob2 = metapieza(5, 5, 2)

        #Postcondición:
        assert ob1.movdiagonal(1) == [(3, 3), (5, 3), (3, 5)]

    def test_case__11(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)
        ob2 = metapieza(5, 5, 2)

        #Postcondición:
        assert ob1.movdiagonal(2) == [(3, 3), (5, 3), (3, 5), (2, 2), (6, 2), (2, 6)]

    def test_case_14(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)
        ob2 = metapieza(3, 3, 2)

        #Postcondición:
        assert ob1.movdiagonal(1) == [(5, 5), (5, 3), (3, 5)]

    def test_case_15(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)
        ob2 = metapieza(3, 3, 2)

        #Postcondición:
        assert ob1.movdiagonal(2) == [(5, 5), (5, 3), (3, 5), (6, 6), (6, 2), (2, 6)]

    def test_case_18(self):

        #Precondición:
        limpiar_matriz()

        ob1 = metapieza(4, 4, 2)

        #Postcondición:
        assert ob1.movdiagonal(0) == []