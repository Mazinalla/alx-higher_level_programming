#!/bin/bash
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    // Check if p is a valid list object
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *item_type = item->ob_type->tp_name;
        printf("Element %zd: %s\n", i, item_type);
    }
}

void print_python_bytes(PyObject *p) {
    // Check if p is a valid bytes object
    if (!PyBytes_Check(p)) {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *bytes_str = PyBytes_AsString(p);

    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python Bytes = %zd\n", size);
    printf("[*] Trying string: %s\n", bytes_str);

    // Print first 10 bytes or the entire string if less than 10 bytes
    printf("first %zd bytes: ", size < 10 ? size : 10);
    for (Py_ssize_t i = 0; i < size && i < 10; i++) {
        printf("%02hhx", bytes_str[i]);
        if (i < 9 && i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}
