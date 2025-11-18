/*
    Archivo: HeapSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento HeapSort (Ordenación por montículo).
*/

namespace MetodosOrdenamiento
{
    public static class HeapSort
    {
        // Método público que ordena el arreglo usando HeapSort
        public static void Sort(int[] a)
        {
            int n = a.Length; // Número de elementos

            // Construimos el heap (montículo) máximo
            for (int i = n / 2 - 1; i >= 0; i--)
            {
                Heapify(a, n, i);
            }

            // Extraemos elementos del heap uno por uno
            for (int i = n - 1; i >= 0; i--)
            {
                // Movemos la raíz (el mayor) al final del arreglo
                int temp = a[0];
                a[0] = a[i];
                a[i] = temp;

                // Llamamos heapify en el subarreglo reducido
                Heapify(a, i, 0);
            }
        }

        // Asegura la propiedad de heap máximo en el subárbol con raíz en i
        private static void Heapify(int[] a, int n, int i)
        {
            int mayor = i;        // Suponemos que la raíz es el mayor
            int izq = 2 * i + 1;  // Índice del hijo izquierdo
            int der = 2 * i + 2;  // Índice del hijo derecho

            // Si el hijo izquierdo existe y es mayor que la raíz
            if (izq < n && a[izq] > a[mayor])
            {
                mayor = izq;
            }

            // Si el hijo derecho existe y es mayor que el mayor actual
            if (der < n && a[der] > a[mayor])
            {
                mayor = der;
            }

            // Si el mayor no es la raíz
            if (mayor != i)
            {
                // Intercambiamos la raíz con el mayor
                int swap = a[i];
                a[i] = a[mayor];
                a[mayor] = swap;

                // Hacemos heapify recursivamente en el subárbol afectado
                Heapify(a, n, mayor);
            }
        }
    }
}
