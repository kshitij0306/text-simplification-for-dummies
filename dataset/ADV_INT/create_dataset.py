# Open the dataset file and create source and target files
with open("ADV-INT.txt", "r") as file, \
     open("ADV.txt", "w") as src_file, \
     open("INT.txt", "w") as target_file:

    # Initialize variables to store source and target sentences
    source_sentence = ""
    target_sentence = ""

    # Process the lines one by one
    for line in file:
        stripped_line = line.strip()

        # Check for the marker line to separate pairs
        if stripped_line.startswith("****"):
            # Write the source and target sentences to their respective files
            src_file.write(source_sentence + "\n")
            target_file.write(target_sentence + "\n")

            # Reset variables for the next pair
            source_sentence = ""
            target_sentence = ""
        else:
            # Determine if it's a source or target sentence based on the line number
            if len(source_sentence) == 0:
                source_sentence = stripped_line
            else:
                target_sentence = stripped_line

    # Write the last pair to their respective files
    src_file.write(source_sentence + "\n")
    target_file.write(target_sentence + "\n")
