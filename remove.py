from rembg import remove

input_image ='animal.jpg'
output_image = 'out.jpg'
with open(input_image,'rb') as i:
    with open(output_image,'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)