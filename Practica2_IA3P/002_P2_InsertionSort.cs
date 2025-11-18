/*
    Archivo: InsertionSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento por Inserción
    basado exactamente en el código que aparece en la guía.
*/

public static class InsertionSort
{
    public static void Sort(int[] array)
    {
        // Recorremos todo el arreglo desde la posición 0 hasta el final
        for (int i = 0; i < array.Length; i++)
        {
            int temp = array[i];        // Guardamos el valor actual
            int j = i - 1;              // Empezamos a comparar hacia atrás

            // Mientras j no salga del arreglo y el valor anterior sea mayor que temp
            while (j >= 0 && array[j] > temp)
            {
                array[j + 1] = array[j]; // Movemos los valores hacia la derecha
                j--;                     // Nos desplazamos hacia atrás
            }

            array[j + 1] = temp;        // Insertamos el valor en la posición correcta
        }
    }
}
