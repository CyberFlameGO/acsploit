import argparse
import Algorithms
import Input

if __name__ == '__main__':
    # move to new class
    parser = argparse.ArgumentParser()
    parser.add_argument("algorithm")
    parser.add_argument("--restraints", action="store_true")
    args = parser.parse_args()

    min_int = 0
    max_int = 2**31 - 1
    
    min_char = 0x61
    max_char = 0x71
    
    min_len = 10
    max_len = 10
    
    n_inputs = 26

    if args.restraints:
        pass
    
    output = None

    # gonna be a big if stack somewhere
    if args.algorithm == "sort":
        algorithm = Algorithms.Sort()
        output = algorithm.exploit(Input.StringGenerator(Input.CharGenerator(min_char, max_char), min_len, max_len), n_inputs)


    # flow networks:
    elif args.algorithm == "fordfulkerson":
        algorithm = Algorithms.FordFulkerson()
        output = algorithm.exploit(Input.IntGenerator(min_int, max_int), n_inputs)

    elif args.algorithm == "pushrelabel":
        algorithm = Algorithms.PushRelabel()
        output = algorithm.exploit(Input.IntGenerator(min_int, max_int), n_inputs)

    elif args.algorithm == "edmondskarp":
        algorithm = Algorithms.EdmondsKarp()
        output = algorithm.exploit(Input.IntGenerator(min_int, max_int), n_inputs)

    # graph Algorithms:
    elif args.algorithm == "dijkstra":
        algorithm = Algorithms.Dijkstra()
        output = algorithm.exploit(Input.StringGenerator(Input.CharGenerator(min_char, max_char), min_len, max_len), n_inputs)

    elif args.algorithm == "fleury":
        algorithm = Algorithms.Fleury()
        output = algorithm.exploit(Input.StringGenerator(Input.CharGenerator(min_char, max_char), min_len, max_len), n_inputs)

    elif args.algorithm == "floydwarshall":
        algorithm = Algorithms.FloydWarshall()
        output = algorithm.exploit(Input.StringGenerator(Input.CharGenerator(min_char, max_char), min_len, max_len), n_inputs)

    elif args.algorithm == "hierholzer":
        algorithm = Algorithms.Hierholzer()
        output = algorithm.exploit(Input.StringGenerator(Input.CharGenerator(min_char, max_char), min_len, max_len), n_inputs)

    elif args.algorithm == "bfs":
        algorithm = Algorithms.BFS()
        output = algorithm.exploit(Input.StringGenerator(Input.CharGenerator(min_char, max_char), min_len, max_len), n_inputs)

    elif args.algorithm == "dfs":
        algorithm = Algorithms.DFS()
        output = algorithm.exploit(Input.StringGenerator(Input.CharGenerator(min_char, max_char), min_len, max_len), n_inputs)


    # finding minimum spanning tree:
    elif args.algorithm == "kruskal":
        algorithm = Algorithms.Kruskal()
        output = algorithm.exploit(Input.IntGenerator(min_int, max_int), n_inputs)

    elif args.algorithm == "prim":
        algorithm = Algorithms.Prim()
        output = algorithm.exploit(Input.IntGenerator(min_int, max_int), n_inputs)


    # string comparison Algorithms:
    elif args.algorithm == "rabinkarp":
        algorithm = Algorithms.RabinKarp()
        output = algorithm.exploit(Input.StringGenerator(Input.CharGenerator(min_char, max_char), min_len, max_len), n_inputs)

    elif args.algorithm == "boyermoore":
        algorithm = Algorithms.BoyerMoore()
        output = algorithm.exploit(Input.StringGenerator(Input.CharGenerator(min_char, max_char), min_len, max_len), n_inputs)


    # Shapes:
    elif args.algorithm == "jarvis":
        algorithm = Algorithms.Jarvis()
        output = algorithm.exploit(Input.IntGenerator(min_int, max_int), n_inputs)

    elif args.algorithm == "graham":
        algorithm = Algorithms.Graham()
        output = algorithm.exploit(Input.IntGenerator(min_int, max_int), n_inputs)

    print(output)
