def decode(message_file):

  with open(message_file,'r') as messagefile:
    lines = messagefile.readlines()

  message_dict = {}
  for line in lines:
    message_dict[int(line.split()[0])] = line.split()[1]


  ends_of_pyramid = list()
  reverse_height = 1
  end_of_level = 1

  for i in range(1, max(message_dict.keys())+1):
    if i == end_of_level:
      ends_of_pyramid.append(i)
      reverse_height += 1
      end_of_level += reverse_height
  
  dictionary_mappings = list()
  for value in ends_of_pyramid:
    dictionary_mappings.append(message_dict[value])

  decoded_file = ' '.join(dictionary_mappings)

  print(decoded_file)

if __name__ == '__main__':
  decode('coding_qual_input.txt')

