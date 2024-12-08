from utils import load
from plp import PLP
import pandas as pd


def main():
    pairs, freqs = load("../data/cds_plp.txt", skip_header=True)
    plp = PLP(ipa_file="../data/ipa_all_test.tsv")

    # Run plp on the first 1000 pairs from the dataset
    plp.train(pairs)
    print(plp)
    # thing = pd.read_csv("../data/ipa_all.csv")
    # thing.to_csv("../data/ipa_all_test.tsv", sep="\t", index=False)

    # Strictly tapping case
    print(plp("weɪtɪŋ"))

    # Strictly raising case
    print(plp("laɪf"))

    # Shouldn't exhibit raising
    print(plp("laɪn"))

    # Interacting case
    print(plp("ksaɪtəd"))

    total = len(pairs)
    errors = 0
    for first, second in pairs:
        if plp(first) != second:
            print(f"UF: {first}\tSF: {second}\tPredicted: {plp(first)}")
            errors += 1

    print(errors / total)


if __name__ == "__main__":
    main()
