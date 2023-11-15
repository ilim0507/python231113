import re

def validate_rrn(rrn):
    # Define the regular expression pattern for a valid South Korean RRN
    pattern = r'^\d{6}-\d{7}$'
    
    # Use re.match to check if the RRN matches the pattern
    match = re.match(pattern, rrn)
    
    if match:
        # Additional checks for more details
        
        # Extract birthdate and personal identification number
        birthdate, personal_id = rrn.split('-')
        
        # Check if the birthdate is valid (e.g., not in the future)
        current_year = int(str(20) + birthdate[:2])  # Assuming 20xx as the current century
        if current_year > 2123:  # Adjust the cutoff year as needed
            return False
        
        month = birthdate[2:4]
        if int(month) > 12:
            return False
        
        date = birthdate[4:6]
        if int(date) > 31:
            return False

        # Check if the first digit of the personal identification number determines gender
        gender_digit = int(personal_id[0])
        is_male = gender_digit % 2 == 1
        
        # Print gender information
        if is_male:
            print("Gender: Male")
        else:
            print("Gender: Female")
        
        # All additional checks passed; the RRN is valid
        return True
    else:
        # If there is no match, the RRN is not valid
        return False

# Example usage
rrn_to_validate = "996825-1234567"  # Replace with the actual RRN
if validate_rrn(rrn_to_validate):
    print(f"{rrn_to_validate} is a valid South Korean RRN.")
else:
    print(f"{rrn_to_validate} is not a valid South Korean RRN.")