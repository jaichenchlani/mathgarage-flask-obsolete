def get_multiplication_facts(str_table_of, str_limit):

    print("Entering get_multiplication_facts...")
    output_dict = {}
    warning_counter = 0
    default_limit = 10
    default_table_of = 13

    output_dict["App Version"] = "v0.1"

    # Perform Validations

    try:
        table_of = int(str_table_of)
    except ValueError:
        # Set the default
        user_message = "Invalid table_of value; Resetting to Default value of {}.".format(default_table_of)
        print(user_message)
        warning_counter = warning_counter + 1
        user_message_key = "Warning" + " " + str(warning_counter)
        output_dict[user_message_key] = user_message
        table_of = default_table_of

    try:
        limit = int(str_limit)
    except ValueError:
        # Set the default
        user_message = "Invalid limit value; Resetting to Default value of {}.".format(default_limit)
        print(user_message)
        warning_counter = warning_counter + 1
        user_message_key = "Warning" + " " + str(warning_counter)
        output_dict[user_message_key] = user_message
        limit = default_limit

    user_message="Generating Multiplication Facts for {} till {}...".format(table_of, limit)
    print(user_message)

    output_key = "Multiplication Facts for {} till {}.".format(table_of, limit)
    output_value = {}

    for i in range(1, limit+1):
        output_value[i] = table_of*i

    output_dict[output_key] = output_value

    user_message = "Final Output: {}".format(output_dict)
    print(user_message)

    user_message = "Process Completed. Returning to Caller."
    print(user_message)
    return str(output_dict) + '\n'