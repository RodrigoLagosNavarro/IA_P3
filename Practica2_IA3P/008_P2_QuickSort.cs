/*
    Archivo: QuickSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento QuickSort (Ordenación Rápida).
*/

namespace MetodosOrdenamiento
{
    public static class QuickSort
    {
        // Método público para ordenar todo el arreglo
        public static void Sort(int[] a)
        {
            QuickSortRec(a, 0, a.Length - 1); // Llamamos al método recursivo
        }

        // Método recursivo que aplica QuickSort en el subarreglo [inicio, fin]
        private static void QuickSortRec(int[] a, int inicio, int fin)
        {
            if (inicio >= fin) return; // Caso base: subarreglo de tamaño 0 o 1

            int i = inicio;                   // Índice que se mueve desde la izquierda
            int j = fin;                      // Índice que se mueve desde la derecha
            int pivote = a[(inicio + fin) / 2]; // Elegimos el elemento central como pivote

            // Particionamiento del arreglo con respecto al pivote
            while (i <= j)
            {
                // Avanzamos i mientras el valor sea menor que el pivote
                while (a[i] < pivote) i++;

                // Retrocedemos j mientras el valor sea mayor que el pivote
                while (a[j] > pivote) j--;

                // Si aún no se cruzan, intercambiamos
                if (i <= j)
                {
                    int aux = a[i];
                    a[i] = a[j];
                    a[j] = aux;

                    i++; // Movemos i hacia la derecha
                    j--; // Movemos j hacia la izquierda
                }
            }

            // Llamamos recursivamente para la parte izquierda del pivote
            if (inicio < j) QuickSortRec(a, inicio, j);

            // Llamamos recursivamente para la parte derecha del pivote
            if (i < fin) QuickSortRec(a, i, fin);
        }
    }
}
