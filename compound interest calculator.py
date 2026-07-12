def main():
    principle = 0
    rate = 0
    years = 0

    while principle <= 0:
        principle = float(input("Enter the principle amount: ").strip())
        if principle <= 0:
            print("Principle can't be less than or equal to zero")

    while rate <= 0:
        rate = float(input("Enter the interest rate: ").strip())
        if rate <= 0:
            print("Interest rate can't be less than or equal to zero")

    while years <= 0:
        years = int(input("Enter the interest time (years): ").strip())
        if years <= 0:
            print("Time can't be less than or equal to zero")

    total = principle * pow((1 + rate / 100), years)
    print(f"Balance after {years} year/s: ${total:.2f}")


if __name__ == "__main__":
    main()