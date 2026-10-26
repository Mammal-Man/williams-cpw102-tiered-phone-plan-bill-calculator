
def exceeds_data_limit(data_used):
    if (data_used > 10):
        return True
    else:
        return False

def get_overage_rate(data_used, has_premium):
    over_rate = 0
    if (data_used <= 20 and data_used > 10):
        if (has_premium):
            over_rate = 1
        else:
            over_rate = 2
    if (data_used > 20):
        if (has_premium):
            over_rate = 2
        else:
            over_rate = 3
    return over_rate

def main():
    GB = float(input("Enter data used (GB): "))
    baseCost = round(float(input("Enter base monthly plan cost: ")), 2)
    premium = input("Do you have a premium plan? (yes or no): ").strip().lower()
    if (premium.startswith('y')):
        has_premium = True
    elif (premium.startswith('n')):
        has_premium = False
    over = exceeds_data_limit(GB)
    overageRate = get_overage_rate(GB, has_premium)
    bill = baseCost
    if (exceeds_data_limit(GB)):
        overAmnt = GB-10
        extraCharge = round(overAmnt*overageRate, 2)
        bill += extraCharge
        print(f"\nYou are {overAmnt} GB over your limit")
        print(f"Overage Rate: ${overageRate} per GB")
    else:
        extraCharge = 0
        print("\nYou are within your data limit.\nGB over limit: 0")
    print(f"Overage Cost: ${extraCharge:.2f}")
    print(f"Total bill: ${bill:.2f}")


# Keep this guard: importing functions for tests must not prompt for input.
if __name__ == "__main__":
    main()
