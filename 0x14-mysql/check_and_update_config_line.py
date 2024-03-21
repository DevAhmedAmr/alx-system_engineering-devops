from fabric.api import * 
env.hosts=["34.227.93.198","54.166.169.232","34.232.65.82"]
env.key_filename=r"C:\Users\ahmed\.ssh\pk3.pem"
env.user="ubuntu"
file_path="/etc/mysql/mysql.conf.d/mysqld.cnf"
database_name="tyrell_corp"

def check_and_update_config_line(target_line, replacement_command, config_file_path):
  """
    This function checks if a specific line exists in a configuration file and updates it if found.
    if not it appends the replacement_command to the file
    Args:
        target_line (str): The line to search for in the configuration file.
        replacement_command (str): The new content to replace the target line with.
        config_file_path (str): The path to the configuration file.

    Returns:
        bool: True if the target line was found and updated, False if it wasn't found.
        """

  with hide("output"):
    # Read the entire file content into a list of lines
    file_content = sudo(f"cat {config_file_path} ").split("\n")

    # Iterate over each line in the file content
    for line_index in range(len(file_content)):
        if file_content[line_index].find(target_line) != -1 :
        # Update the line content
            file_content[line_index] = replacement_command
            print(f"Updated line {line_index}: {file_content[line_index]}")  # Use f-string for formatting

        # Write the updated content back to the file

            sudo(f"printf %s '{"\n".join(file_content)+'\n'}'> {config_file_path}")
            return True

    # If the line wasn't found, append the new command to the end of the file
    sudo(f"echo '{replacement_command+'\n'}' >> {config_file_path}")
    return False