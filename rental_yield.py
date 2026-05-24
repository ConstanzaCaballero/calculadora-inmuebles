def get_float(prompt):
    while True:
        try:
            value = float(input(prompt).replace(",", ""))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("\n=== Rental Yield Calculator ===\n")

    purchase_price = get_float("Purchase price ($): ")
    monthly_rent = get_float("Monthly rent ($): ")
    monthly_expenses = get_float("Monthly expenses (maintenance, insurance, rates, etc.) ($): ")

    annual_rent = monthly_rent * 12
    annual_expenses = monthly_expenses * 12
    annual_net_income = annual_rent - annual_expenses

    gross_yield = (annual_rent / purchase_price) * 100
    net_yield = (annual_net_income / purchase_price) * 100

    print("\n--- Results ---")
    print(f"Annual rent income:    ${annual_rent:,.2f}")
    print(f"Annual expenses:       ${annual_expenses:,.2f}")
    print(f"Annual net income:     ${annual_net_income:,.2f}")
    print(f"\nGross yield:           {gross_yield:.2f}%")
    print(f"Net yield:             {net_yield:.2f}%")

    print("\n--- Recommendation ---")
    if net_yield >= 6:
        verdict = "BUY"
        reason = f"Net yield of {net_yield:.2f}% is strong (≥6%)."
    elif net_yield >= 4:
        verdict = "CONSIDER"
        reason = f"Net yield of {net_yield:.2f}% is acceptable (4–6%) — weigh location and capital growth potential."
    else:
        verdict = "DON'T BUY"
        reason = f"Net yield of {net_yield:.2f}% is weak (<4%) — returns may not justify the investment."

    print(f"Verdict: {verdict}")
    print(f"Reason:  {reason}")
    print()


if __name__ == "__main__":
    main()
