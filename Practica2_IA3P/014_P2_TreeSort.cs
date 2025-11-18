/*
    Archivo: TreeSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento TreeSort
    usando un árbol binario de búsqueda.
*/

namespace MetodosOrdenamiento
{
    public static class TreeSort
    {
        // Clase interna que representa un nodo del árbol
        private class Nodo
        {
            public int Valor; // Valor almacenado en el nodo
            public Nodo Izq;  // Hijo izquierdo
            public Nodo Der;  // Hijo derecho

            public Nodo(int valor)
            {
                Valor = valor; // Inicializamos el valor del nodo
            }
        }

        // Método público para ordenar un arreglo usando TreeSort
        public static void Sort(int[] a)
        {
            if (a.Length == 0) return; // Si el arreglo está vacío, no hacemos nada

            Nodo raiz = null; // Raíz del árbol

            // Insertamos cada elemento del arreglo en el árbol binario
            foreach (int valor in a)
            {
                raiz = Insertar(raiz, valor);
            }

            int index = 0; // Índice para ir llenando el arreglo ordenado

            // Hacemos un recorrido in-order (en-orden) para obtener los elementos ordenados
            InOrder(raiz, a, ref index);
        }

        // Inserta un valor en el árbol binario de búsqueda
        private static Nodo Insertar(Nodo nodo, int valor)
        {
            // Si el nodo es nulo, creamos uno nuevo
            if (nodo == null)
            {
                return new Nodo(valor);
            }

            // Si el valor es menor que el del nodo actual, vamos por la izquierda
            if (valor < nodo.Valor)
            {
                nodo.Izq = Insertar(nodo.Izq, valor);
            }
            else
            {
                // Si es mayor o igual, vamos por la derecha
                nodo.Der = Insertar(nodo.Der, valor);
            }

            return nodo; // Regresamos la referencia al nodo
        }

        // Recorrido en-orden del árbol, guarda los valores ordenados en el arreglo
        private static void InOrder(Nodo nodo, int[] a, ref int index)
        {
            if (nodo == null) return; // Caso base: nodo vacío

            // Primero recorremos el subárbol izquierdo
            InOrder(nodo.Izq, a, ref index);

            // Visitamos el nodo actual: guardamos su valor en el arreglo
            a[index++] = nodo.Valor;

            // Luego recorremos el subárbol derecho
            InOrder(nodo.Der, a, ref index);
        }
    }
}
