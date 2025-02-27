import base64


def insert_decoded_base64_into_jpeg(base64_string, output_filename):
    try:
        decoded_data = base64.b64decode(base64_string)
        
        with open(output_filename, 'wb') as file:
            file.write(decoded_data)
            
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

base64_string = <TODO_add_string_from_link>

success = insert_decoded_base64_into_jpeg(base64_string, "output.jpg")
if success:
    print("Success")
else:
    print("OMG")
  
