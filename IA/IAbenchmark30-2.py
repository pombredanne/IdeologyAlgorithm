import optproblems.cec2005
import numpy as np
import time
from IA import *
import os

def IAalgorithm(n_parties, politicians, R, function, function_index, max_evaluations, desertion_threshold):
    IA = IdeologyAlgorithm(n_parties=n_parties, politicians=politicians, R=R, function=function,
                function_index=function_index, max_evaluations=max_evaluations, desertion_threshold=desertion_threshold)
    return IA.ideology_algorithm()

if __name__ == "__main__":
    dim = 30
    repeats = 10
    evaluations = 10000*dim
    parties = 5
    politicians = 30
    r = 0.5
    desertion_threshold = 10

    if not os.path.exists('results'):
        os.makedirs('results')

    if not os.path.exists('convergence'):
        os.makedirs('convergence')

    np.random.seed(10)

    f2 = optproblems.cec2005.F2(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f2, function_index=2, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-2.txt", "w") as file:
        print("F2: Shifted Schwefel's Problem 1.2", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)

    with open("convergence/IA-convergence-30-2.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)   
    
    f7 = optproblems.cec2005.F7(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f7, function_index=7, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-7.txt", "w") as file:
        print("F7: Shifted Rotated Griewank's Function without Bounds", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-30-7.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f13 = optproblems.cec2005.F13(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f13, function_index=13, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-13.txt", "w") as file:
        print("F13: Expanded Extended Griewank's plus Rosenbrock's Function (F8F2)", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-30-13.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f17 = optproblems.cec2005.F17(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f17, function_index=17, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-17.txt", "w") as file:
        print("F17: Rotated Hybrid Composition Function with Noise in Fitness", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-30-17.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)

    np.random.seed(10)

    f18 = optproblems.cec2005.F18(dim)

    time1 = time.time()
    results = np.array([IAalgorithm(n_parties=parties, politicians=politicians,
        R=r, function=f18, function_index=18, max_evaluations=evaluations,
        desertion_threshold=desertion_threshold) for _ in range(repeats)])
    total_time = time.time() - time1

    means = results.mean(axis=0)
    solutions = results[:,-1]
    mean_best = means[-1]
    min_sol = np.min(solutions)
    max_sol = np.max(solutions)
    marks = means[0:-1]

    with open("results/IA-results-30-18.txt", "w") as file:
        print("F18: Rotated Hybrid Composition Function", file=file)
        print("Min\t Max\t Mean\t Mean time", file=file)
        print("_______________________________________________", file=file)
        print("{} {} {} {}".format(min_sol, max_sol, mean_best, total_time / repeats), file=file)


    with open("convergence/IA-convergence-30-18.csv", "w") as file:
        for i in range(len(marks)):
            print("{},{}".format(10000*i, marks[i]), file=file)
