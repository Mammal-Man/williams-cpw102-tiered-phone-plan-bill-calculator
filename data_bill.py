def check_premium(answer):
    if (answer.strip().lower().startswith('y')):
        return True
    elif (answer.strip().lower().startswith('n')):
        return False

def exceeds_data_limit(data_used):
    if (data_used > 10):
        return True
    else:
        return False

    


def get_overage_rate(data_used, has_premium):
    if (data_used <= 10):
        return 0
    elif (data_used <= 20):
        if (has_premium):
            return 1
        else:
            return 2
    else:
        if (has_premium):
            return 2
        else:
            return 1


def main():
    GB = float(input("Enter GB used: "))
    baseCost = round(float(input("Enter base cost: ")), 2)
    premium = check_premium(input("Are you a premium user (Y/N)? "))
    over = exceeds_data_limit(GB)
    bill = baseCost
    if (exceeds_data_limit(GB)):
        overAmnt = GB-10
        print(f"you are {overAmnt} GB over your limit")
        extraCharge = round(overAmnt*get_overage_rate(GB, premium), 2)
        bill += extraCharge
        if (overAmnt>5):
            usage = 'high'
        else:
            usage = 'moderate'
            print(f"{usage} extra usage.")
    else:
        print("You are within your limit")
    print(f"your bill is ${bill}")   
    if (premium):
        print("Thank you for being a premium member!")
    else:
        print("Consider upgrading to premium for lower overage rates.")


# Keep this guard: importing functions for tests must not prompt for input.
if __name__ == "__main__":
    main()
