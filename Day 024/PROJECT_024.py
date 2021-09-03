
letter_base_lines = []
with open("letter_base.txt", mode="r") as letter_base_file:
    # luetaan kaikki rivit kerralla
    letter_base_lines = letter_base_file.readlines()


with open("names.txt", mode="r") as names_list_file:
    while True:
        # luetaan yksi rivi kerrallaan
        line = names_list_file.readline().replace("\n", "")
        if not line:
            break
        first_line = letter_base_lines[0].replace("[recipient_name]", line)
        with open(f"./ready_letters/{line}.txt", mode="w") as target_file:
            target_file.write(first_line)
            for index in range(1, len(letter_base_lines)):
                target_file.write(letter_base_lines[index])

