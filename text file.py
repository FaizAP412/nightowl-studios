import sys
# Helper function: Read entire file
def read_files(filename):
    with open(filename, "r") as f:
        content = []
        #looping every line in file
        for line in f.readlines():
            content_line = list(line.replace("\n","").split("\t"))
            content.append(content_line)
    return content

# Helper function: Print table headers
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM"))
    print("================================================================")

# Helper function: format for print table
def format_table(counter, line, content):
    format_table = "| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(counter, content[line][0], content[line][1], content[line][2], content[line][3])
    return format_table

# Helper function: Print all content
def print_table(filename):
    try:
        f = open(filename, "r") 
    except:
        print("Maaf file input tidak ada.")

    print_headers()
    content = read_files(filename)
    counter = 1
    #looping every items in list for printing table content
    for i in range(len(content)):
        print(format_table(counter, i, content))
        counter += 1

# Helper function: search and print specific content
def search_phone(filename, key):
        print_headers()
        content = read_files(filename)
        counter = 0
        #Loop untuk setiap items dalam list
        for i in range(len(content)):
            #Search any keyword in list items, using loop for items in nested list    
            if key in content[i][0].lower():
                counter += 1                                
                print(format_table(counter, i, content))
        return counter

# Helper function: get and print descriptive statistics                
def desc_stat(column_num, f, counter):
    content = read_files(f)
    #Mengambil items dari nested list berdasarkan index dari list utama dan index dari list di dalam lis utama 
    match_key = [content[i][column_num] for i in range(len(content))] 
    #Mengubah items dari string menjadi float
    match_key = [float(i) for i in match_key] 
    print("Ukuran data dari hasil pencarian: {} x 4".format(counter))
    print("Min data: {:.2f}".format(min(match_key)))
    print("Max data: {:.2f}".format(max(match_key)))
    print("Rata - rata: {:.2f}".format(sum(match_key)/len(match_key)))

# Main Program
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)

    file_path = sys.argv[1]
    key = sys.argv[2].lower()
    column_num = int(sys.argv[3])

    print_table(file_path)
    print("\n")
    counter = search_phone(file_path, key)
    desc_stat(column_num, file_path, counter)
