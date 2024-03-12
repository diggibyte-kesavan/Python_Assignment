def merge_the_tools(string, k):
    merged_strings = ""
    for i in range(int(len(string) / k)):
        emp_str = ''
        for j in range(k):
            if string[i * k + j] not in emp_str:
                emp_str = emp_str + (string[i * k + j])
        merged_strings += emp_str + "\n"
    return merged_strings.strip()

