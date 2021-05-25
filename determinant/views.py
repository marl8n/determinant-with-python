"""Determinant views"""


from django.shortcuts import render

# Numpy
import numpy as np

def calculate_determinat3x3(request):
    """Returns a result"""
    if request.method == "POST":
        data = np.array([
            [float(request.POST["zero_zero"]), float(request.POST["zero_one"]), float(request.POST["zero_two"])],
            [float(request.POST["one_zero"]), float(request.POST["one_one"]), float(request.POST["one_two"])],
            [float(request.POST["two_zero"]), float(request.POST["two_one"]), float(request.POST["two_two"])],
        ])
        print('estoy en la determinante')
        print(data)
        res = round(np.linalg.det(data), 4)

        return render(request, 'determinant/threexthree.html', {"result": float(res)})
    return render(request, 'determinant/threexthree.html')


def calculate_inv3x3(request):
    """Returns a result"""
    if request.method == "POST":
        data = np.array([
            [float(request.POST["zero_zero"]), float(request.POST["zero_one"]), float(request.POST["zero_two"])],
            [float(request.POST["one_zero"]), float(request.POST["one_one"]), float(request.POST["one_two"])],
            [float(request.POST["two_zero"]), float(request.POST["two_one"]), float(request.POST["two_two"])],
        ])
        print(data)
        res = np.linalg.inv(data)
        print(res)
        return render(request, 'inverse/threexthreeinv.html', {"result": np.array_str(res)})
    return render(request, 'inverse/threexthreeinv.html')


def calculate_determinat4x4(request):
    """Returns a result"""
    if request.method == "POST":
        data = np.array([
            [float(request.POST["zero_zero"]), float(request.POST["zero_one"]), float(request.POST["zero_two"]), float(request.POST["zero_three"])],
            [float(request.POST["one_zero"]), float(request.POST["one_one"]), float(request.POST["one_two"]), float(request.POST["one_three"])],
            [float(request.POST["two_zero"]), float(request.POST["two_one"]), float(request.POST["two_two"]), float(request.POST["two_three"])],
            [float(request.POST["three_zero"]), float(request.POST["three_one"]), float(request.POST["three_two"]), float(request.POST["three_three"])],
        ])
        print(data)
        res = round(np.linalg.det(data), 4)
        return render(request, 'determinant/fourxfour.html', {"result": float(res)})
    return render(request, 'determinant/fourxfour.html')


def calculate_inv4x4(request):
    """Returns a result"""
    if request.method == "POST":
        data = np.array([
            [float(request.POST["zero_zero"]), float(request.POST["zero_one"]), float(request.POST["zero_two"]), float(request.POST["zero_three"])],
            [float(request.POST["one_zero"]), float(request.POST["one_one"]), float(request.POST["one_two"]), float(request.POST["one_three"])],
            [float(request.POST["two_zero"]), float(request.POST["two_one"]), float(request.POST["two_two"]), float(request.POST["two_three"])],
            [float(request.POST["three_zero"]), float(request.POST["three_one"]), float(request.POST["three_two"]), float(request.POST["three_three"])],
        ])
        print(data)
        res =  np.linalg.inv(data)
        return render(request, 'inverse/fourxfourinv.html', {"result": np.array_str(res)})
    return render(request, 'inverse/fourxfourinv.html')