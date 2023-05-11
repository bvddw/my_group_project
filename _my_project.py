with open('input_file.txt', 'r') as f_in, open('output_file.txt', 'w') as f_out:
    ignore_section = False  # прапор, який вказує, чи потрібно ігнорувати поточну секцію
    
    while True:
        line = f_in.readline()
        if not line:
            break
        if '/*' in line:  # початок сесії ігнорування
            ignore_section = True
            before_comment = line.split('/*')[0]  # виводимо частину рядка до символів /*
            if before_comment:
                f_out.write(before_comment)
            continue
        if '*/' in line:  # кінець сесії ігнорування
            ignore_section = False
            line = line.split('*/')[1]  # виводимо частину рядка після символів */
        if ignore_section:  # якщо прапор встановлений, то нічого не виводимо
            continue
        if '/' in line:
            line = line.split('/')[0] + '\n'
        f_out.write(line)
