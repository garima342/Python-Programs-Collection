# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 20:07:55 2025

@author: hp
"""

def process_series(arr):
    n = len(arr)
    half = n // 2

    # Splitting the array into two halves
    first_half = arr[:half]
    second_half = arr[half:]

    # Calculating the product of both halves
    product_first = 1
    product_second = 1

    for num in first_half:
        product_first *= num
    for num in second_half:
        product_second *= num

    # Printing original series
    print("Original series:", arr)

    # Sorting based on condition
    if product_second > product_first:
        arr.sort()
    else:
        arr.sort(reverse=True)

    # Printing modified series
    print("Modified series:", arr)
