# Trebuchet Problem


def part_one() -> None:

    total = 0

    front_pointer = 0
    back_pointer = 0

    #input is "input.txt" given by the first problem

    f = open("./input1.txt", 'r')

    for line in f:

        # Finding first numerical digit from the left then starting 
        # from the right and iterating until numeric is found
        for front_index in range(len(line)):
            if line[front_index].isnumeric():
                front_pointer = int(line[front_index])
                break #ending loop when first index is found 

        for back_index in range(len(line) - 2, -1, -1):
            if line[back_index].isnumeric():
                back_pointer = int(line[back_index])
                break #ending loop when first index is found
     
        #We multiply the front_pointer by 10 in order to make the digit a tens-place digit
        total = (front_pointer*10) + back_pointer + total
    
    #Print result
    print(f"Part One Ans: {total}")

# ---------------------------------------------------------------------------------------------------- #

class digit():

    def __init__(self) -> None:
        # Want a const of strings to compare to as well as its corresponding index for boolean list in below class
        #self.log = open("./log.txt", 'w')
        self.list_of_digits = {"one": 0,
                        "two": 0,
                        "three": 0,
                        "four": 0,
                        "five": 0,
                        "six": 0,
                        "seven": 0,
                        "eight": 0,
                        "nine": 0}
        
        self.reverse_list_of_digits = {"one": 3,
                        "two": 3,
                        "three": 5,
                        "four": 4,
                        "five": 4,
                        "six": 3,
                        "seven": 5,
                        "eight": 5,
                        "nine": 4}

    def input_char_front(self, c: str):
        
        for digit in self.list_of_digits:
            # Checking if char is equal to a potential char in ex. "one", having early termination of checking if bool is false
            if digit[self.list_of_digits[digit]] == c:
                #self.log.write(f"Passed first condition with [{c}] and index: {self.list_of_digits[digit]} on {digit}\n")
                self.list_of_digits[digit]  = self.list_of_digits[digit] + 1

                # Check if we reached the end of the desired string respective of the digit
                if(len(digit)) == self.list_of_digits[digit]:
                    #self.log.write(f"Found! : {digit}")
                    self._reset()
                    return self._return_digit(digit)

            elif digit[0] == c:
                #self.log.write(f"Passed second condition with [{c}] and index: {self.list_of_digits[digit]} on {digit}\n")
                self.list_of_digits[digit] = 1
            else:
                #self.log.write(f"Failed all conditions with [{c}] and index: {self.list_of_digits[digit]} on {digit}\n")
                self.list_of_digits[digit] = 0


    def input_char_back(self, c: str):

        if c != "\n":
            for digit in self.reverse_list_of_digits:
                # Checking if char is equal to a potential char in ex. "one", having early termination of checking if bool is false
                #print(digit[self.reverse_list_of_digits[digit] - 1])
                if digit[self.reverse_list_of_digits[digit] - 1] == c:
                    #self.log.write(f"Passed first condition with [{c}] and index: {self.reverse_list_of_digits[digit]} on {digit}\n")
                    self.reverse_list_of_digits[digit]  = self.reverse_list_of_digits[digit] - 1

                    # Check if we reached the end of the desired string respective of the digit
                    if(0 == self.reverse_list_of_digits[digit]):
                        #self.log.write(f"Found! : {digit}\n")
                        self._reset()
                        return self._return_digit(digit)

                elif digit[0] == c:
                    #self.log.write(f"Passed second condition with [{c}] and index: {self.reverse_list_of_digits[digit]} on {digit}\n")
                    self.reverse_list_of_digits[digit] = self._reset_digit(digit) - 1
                else:
                    #self.log.write(f"Failed all conditions with [{c}] and index: {self.reverse_list_of_digits[digit]} on {digit}\n")
                    self.reverse_list_of_digits[digit] = self._reset_digit(digit)
        else:
            return 0

    # This is to reset the exit condition if discrepency is hit during sequence
    def _reset_digit(self, num: str) -> int:
        # Only avaliable in python 3.10
        match num:
            case "one":
                return 3
            case "two":
                return 3
            case "three":
                return 5
            case "four":
                return 4
            case "five":
                return 4
            case "six":
                return 3
            case "seven":
                return 5
            case "eight":
                return 5
            case "nine":
                return 4
            case _ :
                return 0
    
    def _return_digit(self, num: str) -> int:
        # Only avaliable in python 3.10
        match num:
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9
            case _ :
                return 0

    
    def _reset(self) -> None:
        # Want a const of strings to compare to as well as its corresponding index for boolean list in below class
        self.list_of_digits = {"one": 0,
                        "two": 0,
                        "three": 0,
                        "four": 0,
                        "five": 0,
                        "six": 0,
                        "seven": 0,
                        "eight": 0,
                        "nine": 0}
        
        self.reverse_list_of_digits = {"one": 3,
                        "two": 3,
                        "three": 5,
                        "four": 4,
                        "five": 4,
                        "six": 3,
                        "seven": 5,
                        "eight": 5,
                        "nine": 4}

def part_two() -> None:

    total = 0
    digit_checker = digit()
    ret_back = 0
    ret_foward = 0

    #input is "input.txt" given by the first problem

    f = open("./input1.txt", 'r')

    for line in f:

        # Finding first numerical digit from the left then starting 
        # from the right and iterating until numeric is found
        digit_checker.log.write(line + "\n")
        for front_index in range(len(line)):
            # check if its numeric first
            if line[front_index].isnumeric():
                ret_foward = int(line[front_index])
                digit_checker._reset()
                break #ending loop when first mumeric is found 
            ret_foward = digit_checker.input_char_front(line[front_index])
            if ret_foward != 0 and ret_foward != None:
                break

        for back_index in range(len(line) - 1, -1, -1):
            if line[back_index].isnumeric():
                ret_back = int(line[back_index])
                digit_checker._reset()
                break #ending loop when first index is found
            ret_back = digit_checker.input_char_back(line[back_index])
            if ret_back != 0 and ret_back != None:
                break
     
        #We multiply the front_pointer by 10 in order to make the digit a tens-place digit
        if ret_foward == None:
            ret_foward = 0
        if ret_back == None:
            ret_back = 0
        digit_checker.log.write(f"FWD: {ret_foward} - REV: {ret_back}\n")
        total = (ret_foward*10) + ret_back + total
    
    #Print result
    print(f"Part Two Ans: {total}")

# ---------------------------------------------------------------------------------------------------- #

if __name__ == "__main__":
    part_one()
    part_two()