import sys
import csv


def main():
    with open(sys.argv[2], 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])

        # Write the header only once
        writer.writeheader()

        for row in valid_input():
            last, first = row["name"].split(',')
            writer.writerow({"first": first.strip(), "last": last, "house": row["house"]})


def valid_input():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                return list(csv.DictReader(file))
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
