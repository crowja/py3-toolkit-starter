import argparse


def main():
    ap = argparse.ArgumentParser(prog="mytoolkit XXX")  # TODO
    ap.add_argument("name", help=argparse.SUPPRESS)
    ap.add_argument(
        "-o", "--outfile", default=False, help="Output file name, default stdout"
    )
    args = ap.parse_args()

    # TODO now get up and do what needs to be done ...


if __name__ == "__main__":
    main()
