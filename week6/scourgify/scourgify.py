import sys, csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # def input and output files
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file) as infile:
            reader = csv.DictReader(infile)
            fieldnames = ["first", "last", "house"]
            with open(output_file, "w") as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(",")
                    first = first.strip()
                    writer.writerow(
                        {"first": first, "last": last, "house": row["house"]}
                    )

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == "__main__":
    main()

