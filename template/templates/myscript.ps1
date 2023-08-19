param (
    [string]$DocumentName
)

# Create a new DOCX file
New-Item -Path "$DocumentName.docx" -ItemType File

# Start the DOCX file using the default associated application
Start-Process "$DocumentName.docx"
