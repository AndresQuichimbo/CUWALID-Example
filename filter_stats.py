def filter_lines(input_file, output_file, keyword, start_line=7):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for i, line in enumerate(infile, start=1):
                if i >= start_line and keyword in line:
                    outfile.write(line)
        print(f"Filtered lines containing '{keyword}' have been written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError as e:
        print(f"IO Error: {e}")

if __name__ == '__main__':
    input_filename = 'profiling_stats.txt'
    output_filename = 'filtered_lines.txt'
    keyword_to_search = 'cuwalid'
    
    filter_lines(input_filename, output_filename, keyword_to_search)