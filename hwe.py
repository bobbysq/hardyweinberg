from __future__ import division
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("size", type=int)
parser.add_argument("affected", type=int, help="Number of people with a recessive gene")
parser.add_argument("-d", "--dominant", action="store_true", help="affected is number of dominant people instead of recessive")
parser.add_argument("-n", "--noround", action="store_true", help="Disables rounding")
parser.add_argument("-p", "--percent", action="store_true", help="Expresses as percent")
parser.add_argument("-N", "--number", action="store_true", help="Expresses as numbers. Don't use with -p!")
args = parser.parse_args()

size = args.size
if args.dominant:
    qf = size-args.affected
else:
    qf = args.affected
if args.noround:
    q2  = qf/size
    q   = math.sqrt(q2)
    p   = 1-q
    p2  = p**2
    pq  = 2*p*q
else:
    q2  = round(qf/size, 2)
    q   = round(math.sqrt(q2), 2)
    p   = 1-q
    p2  = round(p**2, 2)
    pq  = round(2*p*q, 2)
if args.number:
    q2  = round(q2*size, 0)
    q   = round(q*size, 0)
    p   = size-q
    p2  = round(p2*size, 0)
    pq  = round(pq*size, 0)
if args.percent:
    print(qf)
    print(size)
    print("p=" + str(100*p) + "%")
    print("q=" + str(100*q) + "%")
    print("p^2 (homozygous dominant)=" + str(100*p2) + "%")
    print("2pq (heterozygous dominant)=" + str(100*pq) + "%")
    print("q^2 (recessive)=" + str(100*q2) + "%")
else:
    print(qf)
    print(size)
    print("p=" + str(p))
    print("q=" + str(q))
    print("p^2 (homozygous dominant)=" + str(p2))
    print("2pq (heterozygous dominant)=" + str(pq))
    print("q^2 (recessive)=" + str(q2))
