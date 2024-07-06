import os


def create_combined_list(folder):
    file_list = os.listdir(folder)
    combined_list = []

    for file in file_list:
        with open(folder + "/" + file,encoding='utf-8') as cur_file:
            combined_list.append([file, 0, []])
            for line in cur_file:
                combined_list[-1][2].append(line.strip())
                combined_list[-1][1] += 1

    return sorted(combined_list, key=lambda x: x[1], reverse=False)


def create_file_from_directory(directory, filename):
    with open(filename + '.txt', 'w+',encoding='utf-8') as newfile:
        for file in create_combined_list(directory):
            newfile.write(f'Название: {file[0]}\n')
            newfile.write(f'Количество строк: {file[1]} string(s)\n')
            for string in file[2]:
                newfile.write(string + '\n')
            newfile.write('\n')


create_file_from_directory('txt', 'mytext')