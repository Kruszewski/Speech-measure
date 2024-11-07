   #!/bin/bash

   # Define the installation directory
   INSTALL_DIR="/usr/local/bin"

   # Check if the user has write permission to the installation directory
   if [ ! -w "$INSTALL_DIR" ]; then
       echo "You do not have write permission to $INSTALL_DIR. Please run as root or use sudo."
       exit 1
   fi

   # Copy the script to the installation directory
   cp main.py "$INSTALL_DIR/mytool"

   # Make the script executable
   chmod +x "$INSTALL_DIR/mytool"

   echo "mytool installed successfully. You can now use it like any other command."