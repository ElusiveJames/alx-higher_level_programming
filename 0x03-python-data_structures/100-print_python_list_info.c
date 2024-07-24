# include <Python.h>
# include <listobject.h>
/**
* print_python_list_info - prints some basic info about Python lists
* @P: list to print
* Return: void
*/

void print_python_list_info(PyObject *P)
{
	int i;

	/* check if its a valid python list */
	if (!PyList_Check(P))
	{
		printf("Invalid list\n");
		return;
	}
	/*cast the list into python object*/
	PyListObject *L = (PyListObject *)P;

	/*print the properties of the list*/
	printf("[*] Size of the Python List = %ld\n", PyList_Size(P));
	printf("[*] Allocated = %ld\n", L->allocated);
	for (i = 0; i < PyList_Size(P); i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(P, i))->tp_name);
	}
}
