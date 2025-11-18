/*
    Archivo: RadixSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento RadixSort
    para números enteros no negativos.
*/

namespace MetodosOrdenamiento
{
    public static class RadixSort
    {
        // Método principal RadixSort
        public static void Sort(int[] a)
        {
            int max = 0; // Guardaremos el valor máximo del arreglo

            // Encontramos el número máximo para saber cuántos dígitos se necesitan
            foreach (int num in a)
            {
                if (num > max)
                    max = num;
            }

            // Ordenamos por cada dígito (unidades, decenas, centenas, etc.)
            for (int exp = 1; max / exp > 0; exp *= 10)
            {
                CountSortByDigit(a, exp);
            }
        }

        // Ordenamiento estable por conteo, según el dígito definido por exp
        private static void CountSortByDigit(int[] a, int exp)
        {
            int n = a.Length;           // Tamaño del arreglo
            int[] output = new int[n];  // Arreglo auxiliar de salida
            int[] count = new int[10];  // Arreglo para contar dígitos (0 a 9)

            // Contamos cuántas veces aparece cada dígito
            for (int i = 0; i < n; i++)
            {
                int index = (a[i] / exp) % 10; // Obtenemos el dígito correspondiente
                count[index]++;                // Incrementamos el contador de ese dígito
            }

            // Transformamos count en posiciones (acumulado)
            for (int i = 1; i < 10; i++)
            {
                count[i] += count[i - 1];
            }

            // Construimos el arreglo de salida (de derecha a izquierda para estabilidad)
            for (int i = n - 1; i >= 0; i--)
            {
                int index = (a[i] / exp) % 10;          // Dígito actual
                output[count[index] - 1] = a[i];        // Colocamos el valor en su posición
                count[index]--;                         // Decrementamos el contador
            }

            // Copiamos los valores ordenados por dígito al arreglo original
            for (int i = 0; i < n; i++)
            {
                a[i] = output[i];
            }
        }
    }
}
