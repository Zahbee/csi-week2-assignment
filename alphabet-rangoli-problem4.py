def print_rangoli(size):
    alphabet = [chr(ord('a') + i) for i in range(size)]
    
    full_width = (size * 4) - 3

    temp_lines = []

    for i in range(size):
        current_level_chars = alphabet[i:size]
        left_segment = '-'.join(current_level_chars[::-1]) 
        
        right_segment = '-'.join(current_level_chars[1:])
        
        line_content = left_segment
        if right_segment:
            line_content += '-' + right_segment
        
        centered_line = line_content.center(full_width, '-')
        temp_lines.append(centered_line)

    result_lines = temp_lines + temp_lines[size-2::-1]
    
    return '\n'.join(result_lines)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
